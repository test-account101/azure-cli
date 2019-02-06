# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps
# pylint: disable=line-too-long, too-many-lines

helps['appservice'] = """
type: group
short-summary: Manage App Service plans.
"""

helps['appservice list-locations'] = """
type: command
short-summary: List regions where a plan sku is available.
examples:
  - name: List regions where a plan sku is available. (crafted)
    text: az appservice list-locations --sku F1
    crafted: true
"""

helps['appservice plan'] = """
type: group
short-summary: Manage app service plans.
"""

helps['appservice plan create'] = """
type: command
short-summary: Create an app service plan.
examples:
  - name: Create a basic app service plan.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan
  - name: Create a standard app service plan with with four Linux workers.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan \\
            --is-linux --number-of-workers 4 --sku S1
"""

helps['appservice plan delete'] = """
type: command
short-summary: Delete an app service plan.
"""

helps['appservice plan list'] = """
type: command
short-summary: List app service plans.
examples:
  - name: List all free tier App Service plans.
    text: >
        az appservice plan list --query "[?sku.tier=='Free']"
"""

helps['appservice plan show'] = """
type: command
short-summary: Get the app service plans for a resource group or a set of resource groups.
examples:
  - name: Get the app service plans for a resource group or a set of resource groups. (commonly used with --output)
    text: az appservice plan show --name MyAppServicePlan  --resource-group MyResourceGroup
    crafted: true
"""

helps['appservice plan update'] = """
type: command
short-summary: Update an app service plan. See https://docs.microsoft.com/en-us/azure/app-service/app-service-plan-manage#move-an-app-to-another-app-service-plan to learn more
examples:
  - name: Update an app service plan. (crafted)
    text: az appservice plan update --name MyAppServicePlan --resource-group MyResourceGroup --sku F1
    crafted: true
"""

helps['functionapp'] = """
type: group
short-summary: Manage function apps.
"""

helps['functionapp config'] = """
type: group
short-summary: Configure a function app.
"""

helps['functionapp config appsettings'] = """
type: group
short-summary: Configure function app settings.
"""

helps['functionapp config appsettings delete'] = """
type: command
short-summary: Delete a function app's settings.
"""

helps['functionapp config appsettings list'] = """
type: command
short-summary: Show settings for a function app.
examples:
  - name: Show settings for a function app. (crafted)
    text: az functionapp config appsettings list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config appsettings set'] = """
type: command
short-summary: Update a function app's settings.
examples:
  - name: Update a function app's settings. (crafted)
    text: az functionapp config appsettings set --name MyFunctionApp --resource-group MyResourceGroup --settings {settings}
    crafted: true
"""

helps['functionapp config container'] = """
type: group
short-summary: Manage function app container settings.
"""

helps['functionapp config container delete'] = """
type: command
short-summary: Delete a function app container's settings.
"""

helps['functionapp config container set'] = """
type: command
short-summary: Set a function app container's settings.
"""

helps['functionapp config container show'] = """
type: command
short-summary: Get details of a function app container's settings.
"""

helps['functionapp config hostname'] = """
type: group
short-summary: Configure hostnames for a function app.
"""

helps['functionapp config hostname add'] = """
type: command
short-summary: Bind a hostname to a function app.
"""

helps['functionapp config hostname delete'] = """
type: command
short-summary: Unbind a hostname from a function app.
"""

helps['functionapp config hostname get-external-ip'] = """
type: command
short-summary: Get the external-facing IP address for a function app.
"""

helps['functionapp config hostname list'] = """
type: command
short-summary: List all hostname bindings for a function app.
"""

helps['functionapp config set'] = """
type: command
short-summary: Set the web app's configuration.
examples:
  - name: Set the web app's configuration. (crafted)
    text: az functionapp config set --min-tls-version {min-tls-version} --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp config show'] = """
type: command
short-summary: Get the details of a web app's configuration.
"""

helps['functionapp config ssl'] = """
type: group
short-summary: Configure SSL certificates.
"""

helps['functionapp config ssl bind'] = """
type: command
short-summary: Bind an SSL certificate to a function app.
examples:
  - name: Bind an SSL certificate to a function app. (crafted)
    text: az functionapp config ssl bind --certificate-thumbprint {certificate-thumbprint} --name MyFunctionApp --resource-group MyResourceGroup --ssl-type SNI
    crafted: true
"""

helps['functionapp config ssl delete'] = """
type: command
short-summary: Delete an SSL certificate from a function app.
"""

helps['functionapp config ssl list'] = """
type: command
short-summary: List SSL certificates for a function app.
"""

helps['functionapp config ssl unbind'] = """
type: command
short-summary: Unbind an SSL certificate from a function app.
"""

helps['functionapp config ssl upload'] = """
type: command
short-summary: Upload an SSL certificate to a function app.
examples:
  - name: Upload an SSL certificate to a function app. (commonly used with --output and --query)
    text: az functionapp config ssl upload --certificate-file {certificate-file} --certificate-password {certificate-password} --name MyFunctionApp     --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp cors'] = """
type: group
short-summary: Manage Cross-Origin Resource Sharing (CORS)
"""

helps['functionapp cors add'] = """
type: command
short-summary: Add allowed origins
examples:
  - name: add a new allowed origin
    text: >
        az functionapp cors add -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
"""

helps['functionapp cors remove'] = """
type: command
short-summary: Remove allowed origins
examples:
  - name: remove an allowed origin
    text: >
        az functionapp cors remove -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
  - name: remove all allowed origins
    text: >
        az functionapp cors remove -g {myRG} -n {myAppName} --allowed-origins *
"""

helps['functionapp cors show'] = """
type: command
short-summary: show allowed origins
"""

helps['functionapp create'] = """
type: command
short-summary: Create a function app.
long-summary: The function app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
  - name: Create a basic function app.
    text: >
        az functionapp create -g MyResourceGroup  -p MyPlan -n MyUniqueAppName -s MyStorageAccount
"""

helps['functionapp delete'] = """
type: command
short-summary: Delete a function app.
examples:
  - name: Delete a function app. (crafted)
    text: az functionapp delete --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment'] = """
type: group
short-summary: Manage function app deployments.
"""

helps['functionapp deployment container'] = """
type: group
short-summary: Manage container-based continuous deployment.
"""

helps['functionapp deployment container config'] = """
type: command
short-summary: Configure continuous deployment via containers.
"""

helps['functionapp deployment container show-cd-url'] = """
type: command
short-summary: Get the URL which can be used to configure webhooks for continuous deployment.
"""

helps['functionapp deployment list-publishing-profiles'] = """
type: command
short-summary: Get the details for available function app deployment profiles.
examples:
  - name: Get the details for available function app deployment profiles. (commonly used with --query)
    text: az functionapp deployment list-publishing-profiles --name MyFunctionApp   --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment source'] = """
type: group
short-summary: Manage function app deployment via source control.
"""

helps['functionapp deployment source config'] = """
type: command
short-summary: Manage deployment from git or Mercurial repositories.
examples:
  - name: Manage deployment from git or Mercurial repositories. (crafted)
    text: az functionapp deployment source config --branch {branch} --name MyFunctionApp --repo-url {repo-url} --repository-type git --resource-group MyResourceGroup
    crafted: true
  - name: Perform deployment using the kudu zip push deployment for a function app. (crafted)
    text: az functionapp deployment source config-zip --name MyFunctionApp --resource-group MyResourceGroup --src {src}
    crafted: true
"""

helps['functionapp deployment source config-local-git'] = """
type: command
short-summary: Get a URL for a git repository endpoint to clone and push to for function app deployment.
examples:
  - name: Get an endpoint and add it as a git remote.
    text: >
        az functionapp deployment source config-local-git \\
            -g MyResourceGroup -n MyUniqueApp

        git remote add azure \\
            https://{deploy_user_name}@MyUniqueApp.scm.azurewebsites.net/MyUniqueApp.git
"""

helps['functionapp deployment source config-zip'] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a function app.
long-summary: >
    By default Kudu assumes that zip deployments do not require any build-related actions like
    npm install or dotnet publish. This can be overridden by including an .deployment file in your
    zip file with the following content '[config] SCM_DO_BUILD_DURING_DEPLOYMENT = true',
    to enable Kudu detection logic and build script generation process.
    See https://github.com/projectkudu/kudu/wiki/Configurable-settings#enabledisable-build-actions-preview.
    Alternately the setting can be enabled using the az functionapp config appsettings set command.
examples:
  - name: Perform deployment by using zip file content.
    text: >
        az functionapp deployment source config-zip \\
            -g {myRG}} -n {myAppName} \\
            --src {zipFilePathLocation}
"""

helps['functionapp deployment source delete'] = """
type: command
short-summary: Delete a source control deployment configuration.
"""

helps['functionapp deployment source show'] = """
type: command
short-summary: Get the details of a source control deployment configuration.
"""

helps['functionapp deployment source sync'] = """
type: command
short-summary: Synchronize from the repository. Only needed under manual integration mode.
examples:
  - name: Synchronize from the repository. Only needed under manual integration mode. (crafted)
    text: az functionapp deployment source sync --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp deployment user'] = """
type: group
short-summary: Manage user credentials for deployment.
"""

helps['functionapp deployment user set'] = """
type: command
short-summary: Update deployment credentials.
long-summary: All function and web apps in the subscription will be impacted since they share the same deployment credentials.
examples:
  - name: Set FTP and git deployment credentials for all apps.
    text: >
        az functionapp deployment user set --user-name MyUserName
"""

helps['functionapp identity'] = """
type: group
short-summary: manage web app's managed service identity
"""

helps['functionapp identity assign'] = """
type: command
short-summary: assign or disable managed service identity to the web app
examples:
  - name: assign local identity and assign a reader role to the current resource group.
    text: >
        az functionapp identity assign -g MyResourceGroup -n MyUniqueApp --role reader --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/MyResourceGroup
  - name: enable identity for the web app.
    text: >
        az functionapp identity assign -g MyResourceGroup -n MyUniqueApp
"""

helps['functionapp identity remove'] = """
type: command
short-summary: Disable web app's managed service identity
"""

helps['functionapp identity show'] = """
type: command
short-summary: display web app's managed service identity
examples:
  - name: display functionapp's managed service identity (commonly used with --output and --query)
    text: az functionapp identity show --name MyFunctionApp     --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp list'] = """
type: command
short-summary: List function apps.
examples:
  - name: List default host name and state for all function apps.
    text: >
        az functionapp list --query "[].{hostName: defaultHostName, state: state}"
  - name: List all running function apps.
    text: >
        az functionapp list --query "[?state=='Running']"
"""

helps['functionapp list-consumption-locations'] = """
type: command
short-summary: List available locations for running function apps.
"""

helps['functionapp plan'] = """
type: group
short-summary: Manage App Service Plans for an Azure Function
"""

helps['functionapp plan create'] = """
type: command
short-summary: Create an App Service Plan for an Azure Function
examples:
  - name: Create a basic app service plan.
    text: >
        az functionapp plan create -g MyResourceGroup -n MyPlan --sku B1
  - name: Create a standard app service plan with with four workers.
    text: >
        az functionapp plan create -g MyResourceGroup -n MyPlan --number-of-workers 4 --sku S1
"""

helps['functionapp restart'] = """
type: command
short-summary: Restart a function app.
examples:
  - name: Restart a function app. (crafted)
    text: az functionapp restart --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp show'] = """
type: command
short-summary: Get the details of a function app.
examples:
  - name: Get the details of a function app. (crafted)
    text: az functionapp show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp start'] = """
type: command
short-summary: Start a function app.
examples:
  - name: Start a function app. (crafted)
    text: az functionapp start --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp stop'] = """
type: command
short-summary: Stop a function app.
examples:
  - name: Stop a function app. (crafted)
    text: az functionapp stop --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps['functionapp update'] = """
type: command
short-summary: Update a function app.
"""

helps['webapp'] = """
type: group
short-summary: Manage web apps.
"""

helps['webapp auth'] = """
type: group
short-summary: Manage webapp authentication and authorization
"""

helps['webapp auth show'] = """
type: command
short-summary: Show the authentification settings for the webapp.
"""

helps['webapp auth update'] = """
type: command
short-summary: Update the authentication settings for the webapp.
examples:
  - name: Enable AAD by enabling authentication and setting AAD-associated parameters. Default provider is set to AAD. Must have created a AAD service principal beforehand.
    text: >
        az webapp auth update  -g myResourceGroup -n myUniqueApp --enabled true \\
          --action LoginWithAzureActiveDirectory \\
          --aad-allowed-token-audiences https://webapp_name.azurewebsites.net/.auth/login/aad/callback \\
          --aad-client-id ecbacb08-df8b-450d-82b3-3fced03f2b27 --aad-client-secret very_secret_password \\
          --aad-token-issuer-url https://sts.windows.net/54826b22-38d6-4fb2-bad9-b7983a3e9c5a/
  - name: Allow Facebook authentication by setting FB-associated parameters and turning on public-profile and email scopes; allow anonymous users
    text: >
        az webapp auth update -g myResourceGroup -n myUniqueApp --action AllowAnonymous \\
          --facebook-app-id my_fb_id --facebook-app-secret my_fb_secret \\
          --facebook-oauth-scopes public_profile email
"""

helps['webapp browse'] = """
type: command
short-summary: Open a web app in a browser.
examples:
  - name: Open a web app in a browser. (crafted)
    text: az webapp browse --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config'] = """
type: group
short-summary: Configure a web app.
"""

helps['webapp config appsettings'] = """
type: group
short-summary: Configure web app settings.
"""

helps['webapp config appsettings delete'] = """
type: command
short-summary: Delete web app settings.
examples:
  - name: Delete web app settings. (crafted)
    text: az webapp config appsettings delete --name MyWebapp --resource-group MyResourceGroup --setting-names {setting-names}
    crafted: true
"""

helps['webapp config appsettings list'] = """
type: command
short-summary: Get the details of a web app's settings.
examples:
  - name: Get the details of a web app's settings. (crafted)
    text: az webapp config appsettings list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config appsettings set'] = """
type: command
short-summary: Set a web app's settings.
examples:
  - name: Set the default NodeJS version to 6.9.1 for a web app.
    text: >
        az webapp config appsettings set -g MyResourceGroup -n MyUniqueApp --settings WEBSITE_NODE_DEFAULT_VERSION=6.9.1
  - name: Set using both key-value pair and a json file with more settings.
    text: >
        az webapp config appsettings set -g MyResourceGroup -n MyUniqueApp --settings mySetting=value @moreSettings.json
"""

helps['webapp config backup'] = """
type: group
short-summary: Manage backups for web apps.
"""

helps['webapp config backup create'] = """
type: command
short-summary: Create a backup of a web app.
"""

helps['webapp config backup list'] = """
type: command
short-summary: List backups of a web app.
"""

helps['webapp config backup restore'] = """
type: command
short-summary: Restore a web app from a backup.
"""

helps['webapp config backup show'] = """
type: command
short-summary: Show the backup schedule for a web app.
"""

helps['webapp config backup update'] = """
type: command
short-summary: Configure a new backup schedule for a web app.
"""

helps['webapp config connection-string'] = """
type: group
short-summary: Manage a web app's connection strings.
"""

helps['webapp config connection-string delete'] = """
type: command
short-summary: Delete a web app's connection strings.
examples:
  - name: Delete a web app's connection strings. (crafted)
    text: az webapp config connection-string delete --name MyWebapp --resource-group MyResourceGroup --setting-names {setting-names}
    crafted: true
"""

helps['webapp config connection-string list'] = """
type: command
short-summary: Get a web app's connection strings.
examples:
  - name: Get a web app's connection strings. (crafted)
    text: az webapp config connection-string list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config connection-string set'] = """
type: command
short-summary: Update a web app's connection strings.
examples:
  - name: Add a mysql connection string.
    text: >
        az webapp config connection-string set -g MyResourceGroup -n MyUniqueApp -t mysql \\
            --settings mysql1='Server=myServer;Database=myDB;Uid=myUser;Pwd=myPwd;'
"""

helps['webapp config container'] = """
type: group
short-summary: Manage web app container settings.
"""

helps['webapp config container delete'] = """
type: command
short-summary: Delete a web app container's settings.
"""

helps['webapp config container set'] = """
type: command
short-summary: Set a web app container's settings.
examples:
  - name: Set a web app container's settings. (crafted)
    text: az webapp config container set --docker-custom-image-name MyDockerCustomImage --docker-registry-server-password {docker-registry-server-password} --docker-registry-server-url {docker-registry-server-url} --docker-registry-server-user {docker-registry-server-user} --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config container show'] = """
type: command
short-summary: Get details of a web app container's settings.
examples:
  - name: Get details of a web app container's settings. (crafted)
    text: az webapp config container show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config hostname'] = """
type: group
short-summary: Configure hostnames for a web app.
"""

helps['webapp config hostname add'] = """
type: command
short-summary: Bind a hostname to a web app.
examples:
  - name: Bind a hostname to a web app. (crafted)
    text: az webapp config hostname add --hostname {hostname} --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config hostname delete'] = """
type: command
short-summary: Unbind a hostname from a web app.
"""

helps['webapp config hostname get-external-ip'] = """
type: command
short-summary: Get the external-facing IP address for a web app.
"""

helps['webapp config hostname list'] = """
type: command
short-summary: List all hostname bindings for a web app.
examples:
  - name: List all hostname bindings for a web app. (crafted)
    text: az webapp config hostname list --resource-group MyResourceGroup --webapp-name MyWebapp
    crafted: true
"""

helps['webapp config set'] = """
type: command
short-summary: Set a web app's configuration.
examples:
  - name: turn on "alwaysOn"
    text: >
        az webapp config set -g MyResourceGroup -n MyUniqueApp --always-on true
  - name: turn on "alwaysOn" through a json with content '{"alwaysOn", true}'
    text: >
        az webapp config set -g MyResourceGroup -n MyUniqueApp --generic-configurations "{"alwaysOn": true}"

"""

helps['webapp config show'] = """
type: command
short-summary: Get the details of a web app's configuration.
examples:
  - name: Get the details of a web app's configuration. (commonly used with --output and --query)
    text: az webapp config show --name MyWebapp     --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config snapshot'] = """
type: group
short-summary: Manage web app snapshots.
"""

helps['webapp config snapshot list'] = """
type: command
short-summary: List the restorable snapshots for a web app.
"""

helps['webapp config snapshot restore'] = """
type: command
short-summary: Restore a web app snapshot.
examples:
  - name: Restore web app files from a snapshot. Overwrites the web app's current files and settings.
    text: >
        az webapp config snapshot restore -g MyResourceGroup -n MySite --time 2018-12-11T23:34:16.8388367
  - name: Restore a snapshot of web app SourceApp to web app TargetApp. Use --restore-content-only to not restore app settings. Overwrites TargetApp's files.
    text: >
        az webapp config snapshot restore -g TargetResourceGroup -n TargetApp --source-name SourceApp --source-resource-group OriginalResourceGroup --time 2018-12-11T23:34:16.8388367 --restore-content-only
"""

helps['webapp config ssl'] = """
type: group
short-summary: Configure SSL certificates for web apps.
"""

helps['webapp config ssl bind'] = """
type: command
short-summary: Bind an SSL certificate to a web app.
examples:
  - name: Bind an SSL certificate to a web app. (crafted)
    text: az webapp config ssl bind --certificate-thumbprint {certificate-thumbprint} --name MyWebapp --resource-group MyResourceGroup --ssl-type SNI
    crafted: true
"""

helps['webapp config ssl delete'] = """
type: command
short-summary: Delete an SSL certificate from a web app.
examples:
  - name: Delete an SSL certificate from a web app. (crafted)
    text: az webapp config ssl delete --certificate-thumbprint {certificate-thumbprint} --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config ssl list'] = """
type: command
short-summary: List SSL certificates for a web app.
examples:
  - name: List SSL certificates for a web app. (crafted)
    text: az webapp config ssl list --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config ssl unbind'] = """
type: command
short-summary: Unbind an SSL certificate from a web app.
"""

helps['webapp config ssl upload'] = """
type: command
short-summary: Upload an SSL certificate to a web app.
examples:
  - name: Upload an SSL certificate to a web app. (commonly used with --output and --query)
    text: az webapp config ssl upload --certificate-file {certificate-file} --certificate-password {certificate-password} --name MyWebapp     --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp config storage-account'] = """
type: group
short-summary: Manage a web app's Azure storage account configurations. (Linux Web Apps and Windows Containers Web Apps Only)
"""

helps['webapp config storage-account add'] = """
type: command
short-summary: Add an Azure storage account configuration to a web app. (Linux Web Apps and Windows Containers Web Apps Only)
examples:
  - name: Add a connection to the Azure Files file share called MyShare in the storage account named MyStorageAccount.
    text: >
        az webapp config storage-account add -g MyResourceGroup -n MyUniqueApp \\
          --custom-id CustomId \\
          --storage-type AzureFiles \\
          --account-name MyStorageAccount \\
          --share-name MyShare \\
          --access-key MyAccessKey \\
          --mount-path /path/to/mount
"""

helps['webapp config storage-account delete'] = """
type: command
short-summary: Delete a web app's Azure storage account configuration. (Linux Web Apps and Windows Containers Web Apps Only)
"""

helps['webapp config storage-account list'] = """
type: command
short-summary: Get a web app's Azure storage account configurations. (Linux Web Apps and Windows Containers Web Apps Only)
"""

helps['webapp config storage-account update'] = """
type: command
short-summary: Update an existing Azure storage account configuration on a web app. (Linux Web Apps and Windows Containers Web Apps Only)
examples:
  - name: Update the mount path for a connection to the Azure Files file share with the ID MyId.
    text: >
        az webapp config storage-account update -g MyResourceGroup -n MyUniqueApp \\
          --custom-id CustomId \\
          --mount-path /path/to/new/mount
"""

helps['webapp cors'] = """
type: group
short-summary: Manage Cross-Origin Resource Sharing (CORS)
"""

helps['webapp cors add'] = """
type: command
short-summary: Add allowed origins
examples:
  - name: add a new allowed origin
    text: >
        az webapp cors add -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
"""

helps['webapp cors remove'] = """
type: command
short-summary: Remove allowed origins
examples:
  - name: remove an allowed origin
    text: >
        az webapp cors remove -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
  - name: remove all allowed origins
    text: >
        az webapp cors remove -g {myRG} -n {myAppName} --allowed-origins *
"""

helps['webapp cors show'] = """
type: command
short-summary: show allowed origins
"""

helps['webapp create'] = """
type: command
short-summary: Create a web app.
long-summary: The web app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
  - name: Create a web app with the default configuration.
    text: >
        az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName
  - name: Create a web app with a NodeJS 6.2 runtime and deployed from a local git repository.
    text: >
        az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName --runtime "node|6.2" --deployment-local-git
"""

helps['webapp delete'] = """
type: command
short-summary: Delete a web app.
examples:
  - name: Delete a web app. (crafted)
    text: az webapp delete --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deleted'] = """
type: group
short-summary: Manage deleted web apps.
"""

helps['webapp deleted list'] = """
type: command
short-summary: List web apps that have been deleted.
"""

helps['webapp deleted restore'] = """
type: command
short-summary: Restore a deleted web app.
long-summary: Restores the files and settings of a deleted web app to the specified web app.
examples:
  - name: Restore a deleted app to the Staging slot of MySite.
    text: >
        az webapp deleted restore -g MyResourceGroup -n MySite -s Staging --deleted-id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Web/deletedSites/1234
  - name: Restore a deleted app to the app MySite. Do not restore the deleted app's settings.
    text: >
        az webapp deleted restore -g MyResourceGroup -n MySite --deleted-id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Web/deletedSites/1234 --restore-content-only
"""

helps['webapp deployment'] = """
type: group
short-summary: Manage web app deployments.
"""

helps['webapp deployment container'] = """
type: group
short-summary: Manage container-based continuous deployment.
"""

helps['webapp deployment container config'] = """
type: command
short-summary: Configure continuous deployment via containers.
examples:
  - name: Configure continuous deployment via containers. (crafted)
    text: az webapp deployment container config --enable-cd true --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment container show-cd-url'] = """
type: command
short-summary: Get the URL which can be used to configure webhooks for continuous deployment.
"""

helps['webapp deployment list-publishing-profiles'] = """
type: command
short-summary: Get the details for available web app deployment profiles.
examples:
  - name: Get the details for available web app deployment profiles. (commonly used with --output and --query)
    text: az webapp deployment list-publishing-profiles --name MyWebapp     --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['webapp deployment slot'] = """
type: group
short-summary: Manage web app deployment slots.
"""

helps['webapp deployment slot auto-swap'] = """
type: command
short-summary: Configure deployment slot auto swap.
"""

helps['webapp deployment slot create'] = """
type: command
short-summary: Create a deployment slot.
examples:
  - name: Create a deployment slot. (crafted)
    text: az webapp deployment slot create --name MyWebapp --resource-group MyResourceGroup --slot {slot}
    crafted: true
"""

helps['webapp deployment slot delete'] = """
type: command
short-summary: Delete a deployment slot.
"""

helps['webapp deployment slot list'] = """
type: command
short-summary: List all deployment slots.
examples:
  - name: List all deployment slots. (crafted)
    text: az webapp deployment slot list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment slot swap'] = """
type: command
short-summary: Change deployment slots for a web app.
examples:
  - name: Swap a staging slot into production for the MyUniqueApp web app.
    text: >
        az webapp deployment slot swap  -g MyResourceGroup -n MyUniqueApp --slot staging \\
            --target-slot production
"""

helps['webapp deployment source'] = """
type: group
short-summary: Manage web app deployment via source control.
"""

helps['webapp deployment source config'] = """
type: command
short-summary: Manage deployment from git or Mercurial repositories.
examples:
  - name: Get a URL for a git repository endpoint to clone and push to for web app deployment. (crafted)
    text: az webapp deployment source config-local-git --name MyWebapp --resource-group MyResourceGroup
    crafted: true
  - name: Perform deployment using the kudu zip push deployment for a webapp. (crafted)
    text: az webapp deployment source config-zip --name MyWebapp --resource-group MyResourceGroup --src {src}
    crafted: true
"""

helps['webapp deployment source config-local-git'] = """
type: command
short-summary: Get a URL for a git repository endpoint to clone and push to for web app deployment.
examples:
  - name: Get an endpoint and add it as a git remote.
    text: >
        az webapp deployment source config-local-git \\
            -g MyResourceGroup -n MyUniqueApp

        git remote add azure \\
            https://{deploy_user_name}@MyUniqueApp.scm.azurewebsites.net/MyUniqueApp.git
"""

helps['webapp deployment source config-zip'] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a web app.
long-summary: >
    By default Kudu assumes that zip deployments do not require any build-related actions like
    npm install or dotnet publish. This can be overridden by including a .deployment file in your
    zip file with the following content '[config] SCM_DO_BUILD_DURING_DEPLOYMENT = true',
    to enable Kudu detection logic and build script generation process.
    See https://github.com/projectkudu/kudu/wiki/Configurable-settings#enabledisable-build-actions-preview.
    Alternately the setting can be enabled using the az webapp config appsettings set command.
examples:
  - name: Perform deployment by using zip file content.
    text: >
        az webapp deployment source config-zip \\
            -g {myRG} -n {myAppName} \\
            --src {zipFilePathLocation}
"""

helps['webapp deployment source delete'] = """
type: command
short-summary: Delete a source control deployment configuration.
"""

helps['webapp deployment source show'] = """
type: command
short-summary: Get the details of a source control deployment configuration.
examples:
  - name: Get the details of a source control deployment configuration. (crafted)
    text: az webapp deployment source show --name MyWebapp --resource-group MyResourceGroup --slot {slot}
    crafted: true
"""

helps['webapp deployment source sync'] = """
type: command
short-summary: Synchronize from the repository. Only needed under manual integration mode.
examples:
  - name: Synchronize from the repository. Only needed under manual integration mode. (crafted)
    text: az webapp deployment source sync --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp deployment user'] = """
type: group
short-summary: Manage user credentials for deployment.
"""

helps['webapp deployment user set'] = """
type: command
short-summary: Update deployment credentials.
long-summary: All function and web apps in the subscription will be impacted since they share the same deployment credentials.
examples:
  - name: Set FTP and git deployment credentials for all apps.
    text: >
        az webapp deployment user set --user-name MyUserName
"""

helps['webapp identity'] = """
type: group
short-summary: manage web app's managed service identity
"""

helps['webapp identity assign'] = """
type: command
short-summary: assign or disable managed service identity to the web app
examples:
  - name: assign local identity and assign a reader role to the current resource group.
    text: >
        az webapp identity assign -g MyResourceGroup -n MyUniqueApp --role reader --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/MyResourceGroup
  - name: enable identity for the web app.
    text: >
        az webapp identity assign -g MyResourceGroup -n MyUniqueApp
"""

helps['webapp identity remove'] = """
type: command
short-summary: Disable web app's managed service identity
"""

helps['webapp identity show'] = """
type: command
short-summary: display web app's managed service identity
examples:
  - name: display webapp's managed service identity (commonly used with --output and --query)
    text: az webapp identity show --name MyWebapp     --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp list'] = """
type: command
short-summary: List web apps.
examples:
  - name: List default host name and state for all web apps.
    text: >
        az webapp list --query "[].{hostName: defaultHostName, state: state}"
  - name: List all running web apps.
    text: >
        az webapp list --query "[?state=='Running']"
"""

helps['webapp list-runtimes'] = """
type: command
short-summary: List available built-in stacks which can be used for web apps.
"""

helps['webapp log'] = """
type: group
short-summary: Manage web app logs.
"""

helps['webapp log config'] = """
type: command
short-summary: Configure logging for a web app.
examples:
  - name: Configure logging for a web app. (crafted)
    text: az webapp log config --name MyWebapp --resource-group MyResourceGroup --web-server-logging off
    crafted: true
"""

helps['webapp log download'] = """
type: command
short-summary: Download a web app's log history as a zip file.
long-summary: This command may not work with web apps running on Linux.
examples:
  - name: Download a web app's log history as a zip file. (crafted)
    text: az webapp log download --log-file {log-file} --name MyWebapp --resource-group MyResourceGroup --slot {slot}
    crafted: true
"""

helps['webapp log show'] = """
type: command
short-summary: Get the details of a web app's logging configuration.
"""

helps['webapp log tail'] = """
type: command
short-summary: Start live log tracing for a web app.
long-summary: This command may not work with web apps running on Linux.
"""

helps['webapp restart'] = """
type: command
short-summary: Restart a web app.
examples:
  - name: Restart a web app. (crafted)
    text: az webapp restart --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp show'] = """
type: command
short-summary: Get the details of a web app.
examples:
  - name: Get the details of a web app. (crafted)
    text: az webapp show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp ssh'] = """
type: command
short-summary: (Preview) SSH command establishes a ssh session to the web container and developer would get a shell terminal remotely.
examples:
  - name: ssh into a web app
    text: >
        az webapp ssh -n MyUniqueAppName -g MyResourceGroup
"""

helps['webapp start'] = """
type: command
short-summary: Start a web app.
examples:
  - name: Start a web app. (crafted)
    text: az webapp start --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp stop'] = """
type: command
short-summary: Stop a web app.
examples:
  - name: Stop a web app. (crafted)
    text: az webapp stop --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp traffic-routing'] = """
type: group
short-summary: Manage traffic routing for web apps.
"""

helps['webapp traffic-routing clear'] = """
type: command
short-summary: Clear the routing rules and send all traffic to production.
"""

helps['webapp traffic-routing set'] = """
type: command
short-summary: Configure routing traffic to deployment slots.
"""

helps['webapp traffic-routing show'] = """
type: command
short-summary: Display the current distribution of traffic across slots.
"""

helps['webapp up'] = """
type: command
short-summary: (Preview) Create and deploy existing local code to the web app, by running the command from the folder where the code is present. Supports running the command in preview mode using --dryrun parameter. Current supports includes Node, Python,.NET Core, ASP.NET, staticHtml. Node, Python apps are created as Linux apps. .Net Core, ASP.NET and static HTML apps are created as Windows apps. If command is run from an empty folder, an empty windows web app is created.
examples:
  - name: View the details of the app that will be created, without actually running the operation
    text: >
        az webapp up -n MyUniqueAppName --dryrun
  - name: Create a web app with the default configuration, by running the command from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName
  - name: Create a web app in a sepcific region, by running the command from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName -l locationName
  - name: Deploy new code to an app that was originally created using the same command
    text: >
        az webapp up -n MyUniqueAppName -l locationName
"""

helps['webapp update'] = """
type: command
short-summary: Update a web app.
examples:
  - name: Update the tags of a web app.
    text: >
        az webapp update -g MyResourceGroup -n MyAppName --set tags.tagName=tagValue
"""

helps['webapp webjob'] = """
type: group
short-summary: Allows management operations for webjobs on a web app.
"""

helps['webapp webjob continuous'] = """
type: group
short-summary: Allows management operations of continuous webjobs on a web app.
"""

helps['webapp webjob continuous list'] = """
type: command
short-summary: List all continuous webjobs on a selected web app.
examples:
  - name: List all continuous webjobs on a selected webapp. (crafted)
    text: az webapp webjob continuous list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp webjob continuous remove'] = """
type: command
short-summary: Delete a specific continuous webjob.
"""

helps['webapp webjob continuous start'] = """
type: command
short-summary: Start a specific continuous webjob on a selected web app.
"""

helps['webapp webjob continuous stop'] = """
type: command
short-summary: Stop a specific continuous webjob.
"""

helps['webapp webjob triggered'] = """
type: group
short-summary: Allows management operations of triggered webjobs on a web app.
"""

helps['webapp webjob triggered list'] = """
type: command
short-summary: List all triggered webjobs hosted on a web app.
"""

helps['webapp webjob triggered log'] = """
type: command
short-summary: Get history of a specific triggered webjob hosted on a web app.
"""

helps['webapp webjob triggered remove'] = """
type: command
short-summary: Delete a specific triggered webjob hosted on a web app.
"""

helps['webapp webjob triggered run'] = """
type: command
short-summary: Run a specific triggered webjob hosted on a web app.
"""
