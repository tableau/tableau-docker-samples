import argparse
import logging

import tableauserverclient as TSC
from tableauserverclient import ConnectionCredentials, ConnectionItem

def main():

    parser = argparse.ArgumentParser(description='Publish a data source to server.')
    parser.add_argument('--server', '-s', required=True, help='server address')
    parser.add_argument('--username', '-u', required=True, help='username to sign into server')
    parser.add_argument('--password', '-p', required=True, help='password to sign into server')
    parser.add_argument('--filepath', '-f', required=True, help='filepath to the datasource to publish')
    parser.add_argument('--project', '-pr', required=True, help='target project') 
    parser.add_argument('--logging-level', '-l', choices=['debug', 'info', 'error'], default='error',
                        help='desired logging level (set to error by default)')
    parser.add_argument('--as-job', '-a', help='Publishing asynchronously', action='store_true')
    parser.add_argument('--siteid', '-si', help='target site')

    args = parser.parse_args()

    # Set logging level based on user input, or error by default
    logging_level = getattr(logging, args.logging_level.upper())
    logging.basicConfig(level=logging_level)

    # Step 1: Sign in to server.
    tableau_auth = TSC.TableauAuth(args.username, args.password)

    if args.siteid is not None:
        tableau_auth.siteid = args.siteid

    server = TSC.Server(args.server)

    server.add_http_options({'verify': False})

    overwrite_true = TSC.Server.PublishMode.Overwrite

    with server.auth.sign_in(tableau_auth):
        
        # Step 2: Get all the projects on server, then look for the default one.
        all_projects, pagination_item = server.projects.get()

        project = next((p for p in all_projects if p.name.lower() == args.project.lower()), None)

        # Step 3: If default project is found, form a new workbook item and publish.
        if project is not None:
            new_ds = TSC.DatasourceItem(project.id)
        
            if args.as_job:
                new_job = server.datasources.publish(new_ds, args.filepath, server.PublishMode.Overwrite, as_job=args.as_job)
                print("Datasource published.JOB ID: {0}".format(new_job.id))
            else:
                new_ds = server.datasources.publish(new_ds, args.filepath, server.PublishMode.Overwrite, as_job=args.as_job)

                print("Datasource published. ID: {0}".format(new_ds.id))
        else:
            error = "The default project could not be found."
            raise LookupError(error)


if __name__ == '__main__':
    main()
