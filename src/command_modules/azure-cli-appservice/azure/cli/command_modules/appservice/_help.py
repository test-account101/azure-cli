# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps["appservice"] = """
type: group
short-summary: Manage App Service plans.
"""

helps["appservice list-locations"] = """
type: command
short-summary: List regions where a plan sku is available.
"""

helps["appservice plan"] = """
type: group
short-summary: Manage app service plans.
"""

helps["appservice plan create"] = """
type: command
short-summary: Create an app service plan.
examples:
-   name: Create a basic app service plan.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan
-   name: Create a standard app service plan with with four Linux workers.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan     --is-linux --number-of-workers
        4 --sku S1
-   name: Create an app service plan.
    text: az appservice plan create --name MyPlan --sku B1 --resource-group MyResourceGroup
    crafted: 'True'
-   name: Create an app service plan.
    text: az appservice plan create --name MyPlan --sku B1 --resource-group MyResourceGroup
    crafted: true
"""

helps["appservice plan delete"] = """
type: command
short-summary: Delete an app service plan.
"""

helps["appservice plan list"] = """
type: command
short-summary: List app service plans.
examples:
-   name: List all free tier App Service plans.
    text: >
        az appservice plan list --query "[?sku.tier=='Free']"
-   name: List app service plans.
    text: az appservice plan list --resource-group MyResourceGroup
    crafted: 'True'
-   name: List app service plans.
    text: az appservice plan list --resource-group MyResourceGroup
    crafted: true
"""

helps["appservice plan show"] = """
type: command
short-summary: Get the app service plans for a resource group or a set of resource
    groups.
examples:
-   name: Get the app service plans for a resource group or a set of resource groups.
    text: az appservice plan show --output json --resource-group MyResourceGroup --name
        MyAppServicePlan
    crafted: 'True'
-   name: Get the app service plans for a resource group or a set of resource groups.
    text: az appservice plan show --output json --resource-group MyResourceGroup --name
        MyAppServicePlan
    crafted: true
"""

helps["appservice plan update"] = """
type: command
short-summary: Update an app service plan.
examples:
-   name: Update an app service plan.
    text: az appservice plan update --resource-group MyResourceGroup --sku B1 --name
        MyAppServicePlan
    crafted: 'True'
-   name: Update an app service plan.
    text: az appservice plan update --resource-group MyResourceGroup --sku B1 --name
        MyAppServicePlan
    crafted: true
"""

helps["functionapp"] = """
type: group
short-summary: Manage function apps.
"""

helps["functionapp config"] = """
type: group
short-summary: Configure a function app.
"""

helps["functionapp config appsettings"] = """
type: group
short-summary: Configure function app settings.
"""

helps["functionapp config appsettings delete"] = """
type: command
short-summary: Delete a function app's settings.
"""

helps["functionapp config appsettings list"] = """
type: command
short-summary: Show settings for a function app.
examples:
-   name: Show settings for a function app.
    text: az functionapp config appsettings list --resource-group MyResourceGroup
        --name MyWebapp
    crafted: 'True'
-   name: Show settings for a function app.
    text: az functionapp config appsettings list --resource-group MyResourceGroup
        --name MyWebapp
    crafted: true
"""

helps["functionapp config appsettings set"] = """
type: command
short-summary: Update a function app's settings.
examples:
-   name: Update a function app's settings.
    text: az functionapp config appsettings set --settings {settings} --resource-group
        MyResourceGroup --name MyFunctionApp
    crafted: 'True'
-   name: Update a function app's settings.
    text: az functionapp config appsettings set --settings {settings} --resource-group
        MyResourceGroup --name MyFunctionApp
    crafted: true
"""

helps["functionapp config hostname"] = """
type: group
short-summary: Configure hostnames for a function app.
"""

helps["functionapp config hostname add"] = """
type: command
short-summary: Bind a hostname to a function app.
"""

helps["functionapp config hostname delete"] = """
type: command
short-summary: Unbind a hostname from a function app.
"""

helps["functionapp config hostname get-external-ip"] = """
type: command
short-summary: Get the external-facing IP address for a function app.
"""

helps["functionapp config hostname list"] = """
type: command
short-summary: List all hostname bindings for a function app.
"""

helps["functionapp config set"] = """
type: command
short-summary: Set the web app's configuration.
"""

helps["functionapp config show"] = """
type: command
short-summary: Get the details of a web app's configuration.
"""

helps["functionapp config ssl"] = """
type: group
short-summary: Configure SSL certificates.
"""

helps["functionapp config ssl bind"] = """
type: command
short-summary: Bind an SSL certificate to a function app.
examples:
-   name: Bind an SSL certificate to a function app.
    text: az functionapp config ssl bind --ssl-type IP --resource-group MyResourceGroup
        --certificate-thumbprint {certificate-thumbprint} --name MyFunctionApp
    crafted: 'True'
-   name: Bind an SSL certificate to a function app.
    text: az functionapp config ssl bind --ssl-type IP --resource-group MyResourceGroup
        --certificate-thumbprint {certificate-thumbprint} --name MyFunctionApp
    crafted: true
"""

helps["functionapp config ssl delete"] = """
type: command
short-summary: Delete an SSL certificate from a function app.
"""

helps["functionapp config ssl list"] = """
type: command
short-summary: List SSL certificates for a function app.
"""

helps["functionapp config ssl unbind"] = """
type: command
short-summary: Unbind an SSL certificate from a function app.
"""

helps["functionapp config ssl upload"] = """
type: command
short-summary: Upload an SSL certificate to a function app.
examples:
-   name: Upload an SSL certificate to a function app.
    text: az functionapp config ssl upload --certificate-password {certificate-password}
        --query [0] --certificate-file {certificate-file} --resource-group MyResourceGroup
        --output json --name MyFunctionApp
    crafted: 'True'
-   name: Upload an SSL certificate to a function app.
    text: az functionapp config ssl upload --certificate-password {certificate-password}
        --query [0] --certificate-file {certificate-file} --resource-group MyResourceGroup
        --output json --name MyFunctionApp
    crafted: true
"""

helps["functionapp cors"] = """
type: group
short-summary: Manage Cross-Origin Resource Sharing (CORS)
"""

helps["functionapp cors add"] = """
type: command
short-summary: Add allowed origins
examples:
-   name: add a new allowed origin
    text: >
        az functionapp cors add -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
-   name: Add allowed origins.
    text: az functionapp cors add --resource-group {myRG} --allowed-origins https://myapps.com
        --name {myAppName}
    crafted: 'True'
-   name: Add allowed origins.
    text: az functionapp cors add --resource-group {myRG} --allowed-origins https://myapps.com
        --name {myAppName}
    crafted: true
"""

helps["functionapp cors remove"] = """
type: command
short-summary: Remove allowed origins
examples:
-   name: remove an allowed origin
    text: >
        az functionapp cors remove -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
-   name: remove all allowed origins
    text: >
        az functionapp cors remove -g {myRG} -n {myAppName} --allowed-origins *
-   name: Remove allowed origins.
    text: az functionapp cors remove --resource-group {myRG} --allowed-origins https://myapps.com
        --name {myAppName}
    crafted: 'True'
-   name: Remove allowed origins.
    text: az functionapp cors remove --resource-group {myRG} --allowed-origins https://myapps.com
        --name {myAppName}
    crafted: true
"""

helps["functionapp cors show"] = """
type: command
short-summary: show allowed origins
"""

helps["functionapp create"] = """
type: command
short-summary: Create a function app.
long-summary: The function app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
-   name: Create a basic function app.
    text: >
        az functionapp create -g MyResourceGroup  -p MyPlan -n MyUniqueAppName -s
        MyStorageAccount
-   name: Create a function app.
    text: az functionapp create --consumption-plan-location {consumption-plan-location}
        --storage-account MyStorageAccount --resource-group MyResourceGroup  --name
        MyUniqueAppName
    crafted: 'True'
-   name: Create a function app.
    text: az functionapp create --consumption-plan-location {consumption-plan-location}
        --storage-account MyStorageAccount --resource-group MyResourceGroup  --name
        MyUniqueAppName
    crafted: true
"""

helps["functionapp delete"] = """
type: command
short-summary: Delete a function app.
examples:
-   name: Delete a function app.
    text: az functionapp delete --resource-group MyResourceGroup --name MyFunctionApp
    crafted: 'True'
-   name: Delete a function app.
    text: az functionapp delete --resource-group MyResourceGroup --name MyFunctionApp
    crafted: true
"""

helps["functionapp deployment"] = """
type: group
short-summary: Manage function app deployments.
"""

helps["functionapp deployment list-publishing-profiles"] = """
type: command
short-summary: Get the details for available function app deployment profiles.
"""

helps["functionapp deployment source"] = """
type: group
short-summary: Manage function app deployment via source control.
"""

helps["functionapp deployment source config"] = """
type: command
short-summary: Manage deployment from git or Mercurial repositories.
"""

helps["functionapp deployment source config-local-git"] = """
type: command
short-summary: Get a URL for a git repository endpoint to clone and push to for function
    app deployment.
examples:
-   name: Get an endpoint and add it as a git remote.
    text: >
        az functionapp deployment source config-local-git \\
            -g MyResourceGroup -n MyUniqueApp

        git remote add azure \\
            https://{deploy_user_name}@MyUniqueApp.scm.azurewebsites.net/MyUniqueApp.git
"""

helps["functionapp deployment source config-zip"] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a function
    app.
long-summary: >
    By default Kudu assumes that zip deployments do not require any build-related
    actions like
    npm install or dotnet publish. This can be overridden by including an .deployment
    file in your
    zip file with the following content '[config] SCM_DO_BUILD_DURING_DEPLOYMENT =
    true',
    to enable Kudu detection logic and build script generation process.
    See https://github.com/projectkudu/kudu/wiki/Configurable-settings#enabledisable-build-actions-preview.
    Alternately the setting can be enabled using the az functionapp config appsettings
    set command.
examples:
-   name: Perform deployment by using zip file content.
    text: >
        az functionapp deployment source config-zip     -g {myRG} -n {myAppName}     --src
        {zip file path location}
-   name: Perform deployment using the kudu zip push deployment for a function app.
    text: az functionapp deployment source config-zip --src {src} --name MyFunctionApp
        --resource-group MyResourceGroup
    crafted: 'True'
-   name: Perform deployment using the kudu zip push deployment for a function app.
    text: az functionapp deployment source config-zip --src {src} --name MyFunctionApp
        --resource-group MyResourceGroup
    crafted: true
"""

helps["functionapp deployment source delete"] = """
type: command
short-summary: Delete a source control deployment configuration.
"""

helps["functionapp deployment source show"] = """
type: command
short-summary: Get the details of a source control deployment configuration.
"""

helps["functionapp deployment source sync"] = """
type: command
short-summary: Synchronize from the repository. Only needed under manual integration
    mode.
examples:
-   name: Synchronize from the repository. Only needed under manual integration mode.
    text: az functionapp deployment source sync --resource-group MyResourceGroup --name
        MyFunctionApp
    crafted: 'True'
-   name: Synchronize from the repository. Only needed under manual integration mode.
    text: az functionapp deployment source sync --resource-group MyResourceGroup --name
        MyFunctionApp
    crafted: true
"""

helps["functionapp deployment user"] = """
type: group
short-summary: Manage user credentials for deployment.
"""

helps["functionapp deployment user set"] = """
type: command
short-summary: Update deployment credentials.
long-summary: All function and web apps in the subscription will be impacted since
    they share the same deployment credentials.
examples:
-   name: Set FTP and git deployment credentials for all apps.
    text: >
        az functionapp deployment user set --user-name MyUserName
"""

helps["functionapp identity"] = """
type: group
short-summary: manage functionapp's managed service identity
"""

helps["functionapp identity assign"] = """
type: command
short-summary: assign or disable managed service identity to the functionapp
examples:
-   name: assign local identity and assign a reader role to the current resource group.
    text: >
        az functionapp identity assign -g MyResourceGroup -n MyUniqueApp --role reader
        --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/MyResourceGroup
-   name: enable identity for the functionapp.
    text: >
        az functionapp identity assign -g MyResourceGroup -n MyUniqueApp
"""

helps["functionapp identity remove"] = """
type: command
short-summary: Disable functionapp's managed service identity
"""

helps["functionapp identity show"] = """
type: command
short-summary: display functionapp's managed service identity
examples:
-   name: Display functionapp's managed service identity.
    text: az functionapp identity show --output json --resource-group MyResourceGroup
        --query [0] --name MyFunctionApp
    crafted: 'True'
-   name: Display functionapp's managed service identity.
    text: az functionapp identity show --output json --resource-group MyResourceGroup
        --query [0] --name MyFunctionApp
    crafted: true
"""

helps["functionapp list"] = """
type: command
short-summary: List function apps.
examples:
-   name: List default host name and state for all function apps.
    text: >
        az functionapp list --query "[].{hostName: defaultHostName, state: state}"
-   name: List all running function apps.
    text: >
        az functionapp list --query "[?state=='Running']"
-   name: List function apps.
    text: az functionapp list --output json
    crafted: 'True'
-   name: List function apps.
    text: az functionapp list --output json
    crafted: true
"""

helps["functionapp list-consumption-locations"] = """
type: command
short-summary: List available locations for running function apps.
"""

helps["functionapp restart"] = """
type: command
short-summary: Restart a function app.
examples:
-   name: Restart a function app.
    text: az functionapp restart --resource-group MyResourceGroup --name MyFunctionApp
    crafted: 'True'
-   name: Restart a function app.
    text: az functionapp restart --resource-group MyResourceGroup --name MyFunctionApp
    crafted: true
"""

helps["functionapp show"] = """
type: command
short-summary: Get the details of a function app.
examples:
-   name: Get the details of a function app.
    text: az functionapp show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Get the details of a function app.
    text: az functionapp show --name MyFunctionApp --resource-group MyResourceGroup
    crafted: true
"""

helps["functionapp start"] = """
type: command
short-summary: Start a function app.
examples:
-   name: Start a function app.
    text: az functionapp start --resource-group MyResourceGroup --name MyFunctionApp
    crafted: 'True'
-   name: Start a function app.
    text: az functionapp start --resource-group MyResourceGroup --name MyFunctionApp
    crafted: true
"""

helps["functionapp stop"] = """
type: command
short-summary: Stop a function app.
examples:
-   name: Stop a function app.
    text: az functionapp stop --resource-group MyResourceGroup --name MyFunctionApp
    crafted: 'True'
-   name: Stop a function app.
    text: az functionapp stop --resource-group MyResourceGroup --name MyFunctionApp
    crafted: true
"""

helps["functionapp update"] = """
type: command
short-summary: Update a function app.
"""

helps["webapp"] = """
type: group
short-summary: Manage web apps.
examples:
-   name: Creates a remote connection using a tcp tunnel to your web app.
    text: az webapp remote-connection create --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
"""

helps["webapp auth"] = """
type: group
short-summary: Manage webapp authentication and authorization
"""

helps["webapp auth show"] = """
type: command
short-summary: Show the authentification settings for the webapp.
"""

helps["webapp auth update"] = """
type: command
short-summary: Update the authentication settings for the webapp.
examples:
-   name: Enable AAD by enabling authentication and setting AAD-associated parameters.
        Default provider is set to AAD. Must have created a AAD service principal
        beforehand.
    text: >
        az webapp auth update  -g myResourceGroup -n myUniqueApp --enabled true \\
          --action LoginWithAzureActiveDirectory \\
          --aad-allowed-token-audiences https://webapp_name.azurewebsites.net/.auth/login/aad/callback
        \\
          --aad-client-id ecbacb08-df8b-450d-82b3-3fced03f2b27 --aad-client-secret
        very_secret_password \\
          --aad-token-issuer-url https://sts.windows.net/54826b22-38d6-4fb2-bad9-b7983a3e9c5a/
-   name: Allow Facebook authentication by setting FB-associated parameters and turning
        on public-profile and email scopes; allow anonymous users
    text: >
        az webapp auth update -g myResourceGroup -n myUniqueApp --action AllowAnonymous
        \\
          --facebook-app-id my_fb_id --facebook-app-secret my_fb_secret \\
          --facebook-oauth-scopes public_profile email
"""

helps["webapp browse"] = """
type: command
short-summary: Open a web app in a browser.
"""

helps["webapp config"] = """
type: group
short-summary: Configure a web app.
"""

helps["webapp config appsettings"] = """
type: group
short-summary: Configure web app settings.
"""

helps["webapp config appsettings delete"] = """
type: command
short-summary: Delete web app settings.
examples:
-   name: Delete web app settings.
    text: az webapp config appsettings delete --name MyWebapp --setting-names {setting-names}
        --resource-group MyResourceGroup
    crafted: 'True'
-   name: Delete web app settings.
    text: az webapp config appsettings delete --name MyWebapp --setting-names {setting-names}
        --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config appsettings list"] = """
type: command
short-summary: Get the details of a web app's settings.
examples:
-   name: Get the details of a web app's settings.
    text: az webapp config appsettings list --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Get the details of a web app's settings.
    text: az webapp config appsettings list --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config appsettings set"] = """
type: command
short-summary: Set a web app's settings.
examples:
-   name: Set the default NodeJS version to 6.9.1 for a web app.
    text: >
        az webapp config appsettings set -g MyResourceGroup -n MyUniqueApp --settings
        WEBSITE_NODE_DEFAULT_VERSION=6.9.1
-   name: Set a web app's settings.
    text: az webapp config appsettings set --settings WEBSITE_NODE_DEFAULT_VERSION=6.9.1
        --name MyUniqueApp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Set a web app's settings.
    text: az webapp config appsettings set --settings WEBSITE_NODE_DEFAULT_VERSION=6.9.1
        --name MyUniqueApp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config backup"] = """
type: group
short-summary: Manage backups for web apps.
"""

helps["webapp config backup create"] = """
type: command
short-summary: Create a backup of a web app.
"""

helps["webapp config backup list"] = """
type: command
short-summary: List backups of a web app.
"""

helps["webapp config backup restore"] = """
type: command
short-summary: Restore a web app from a backup.
"""

helps["webapp config backup show"] = """
type: command
short-summary: Show the backup schedule for a web app.
"""

helps["webapp config backup update"] = """
type: command
short-summary: Configure a new backup schedule for a web app.
"""

helps["webapp config connection-string"] = """
type: group
short-summary: Manage a web app's connection strings.
"""

helps["webapp config connection-string delete"] = """
type: command
short-summary: Delete a web app's connection strings.
"""

helps["webapp config connection-string list"] = """
type: command
short-summary: Get a web app's connection strings.
examples:
-   name: Get a web app's connection strings.
    text: az webapp config connection-string list --name MyWebapp --resource-group
        MyResourceGroup
    crafted: 'True'
-   name: Get a web app's connection strings.
    text: az webapp config connection-string list --name MyWebapp --resource-group
        MyResourceGroup
    crafted: true
"""

helps["webapp config connection-string set"] = """
type: command
short-summary: Update a web app's connection strings.
examples:
-   name: Add a mysql connection string.
    text: >
        az webapp config connection-string set -g MyResourceGroup -n MyUniqueApp -t
        mysql     --settings mysql1='Server=myServer;Database=myDB;Uid=myUser;Pwd=myPwd;'
-   name: Update a web app's connection strings.
    text: az webapp config connection-string set --settings {settings} --connection-string-type
        ApiHub --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Update a web app's connection strings.
    text: az webapp config connection-string set --settings {settings} --connection-string-type
        ApiHub --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config container"] = """
type: group
short-summary: Manage web app container settings.
"""

helps["webapp config container delete"] = """
type: command
short-summary: Delete a web app container's settings.
"""

helps["webapp config container set"] = """
type: command
short-summary: Set a web app container's settings.
examples:
-   name: Set a web app container's settings.
    text: az webapp config container set --docker-registry-server-password {docker-registry-server-password}
        --docker-custom-image-name MyDockerCustomImage --resource-group MyResourceGroup
        --docker-registry-server-url {docker-registry-server-url} --name MyWebapp
        --docker-registry-server-user {docker-registry-server-user}
    crafted: 'True'
-   name: Set a web app container's settings.
    text: az webapp config container set --docker-registry-server-password {docker-registry-server-password}
        --docker-custom-image-name MyDockerCustomImage --resource-group MyResourceGroup
        --docker-registry-server-url {docker-registry-server-url} --name MyWebapp
        --docker-registry-server-user {docker-registry-server-user}
    crafted: true
"""

helps["webapp config container show"] = """
type: command
short-summary: Get details of a web app container's settings.
"""

helps["webapp config hostname"] = """
type: group
short-summary: Configure hostnames for a web app.
"""

helps["webapp config hostname add"] = """
type: command
short-summary: Bind a hostname to a web app.
examples:
-   name: Bind a hostname to a web app.
    text: az webapp config hostname add --webapp-name MyWebapp --hostname {hostname}
        --resource-group MyResourceGroup
    crafted: 'True'
-   name: Bind a hostname to a web app.
    text: az webapp config hostname add --webapp-name MyWebapp --hostname {hostname}
        --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config hostname delete"] = """
type: command
short-summary: Unbind a hostname from a web app.
"""

helps["webapp config hostname get-external-ip"] = """
type: command
short-summary: Get the external-facing IP address for a web app.
"""

helps["webapp config hostname list"] = """
type: command
short-summary: List all hostname bindings for a web app.
examples:
-   name: List all hostname bindings for a web app.
    text: az webapp config hostname list --webapp-name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: List all hostname bindings for a web app.
    text: az webapp config hostname list --webapp-name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config set"] = """
type: command
short-summary: Set a web app's configuration.
examples:
-   name: Set a web app's configuration.
    text: az webapp config set --always-on false --resource-group MyResourceGroup
        --name MyWebapp
    crafted: 'True'
-   name: Set a web app's configuration.
    text: az webapp config set --always-on false --resource-group MyResourceGroup
        --name MyWebapp
    crafted: true
"""

helps["webapp config show"] = """
type: command
short-summary: Get the details of a web app's configuration.
examples:
-   name: Get the details of a web app's configuration.
    text: az webapp config show --output json --name MyWebapp --query [0] --resource-group
        MyResourceGroup
    crafted: 'True'
-   name: Get the details of a web app's configuration.
    text: az webapp config show --output json --name MyWebapp --query [0] --resource-group
        MyResourceGroup
    crafted: true
"""

helps["webapp config snapshot"] = """
type: group
short-summary: Manage web app snapshots.
"""

helps["webapp config snapshot list"] = """
type: command
short-summary: List the restorable snapshots for a web app.
"""

helps["webapp config snapshot restore"] = """
type: command
short-summary: Restore a web app snapshot.
examples:
-   name: Restore web app files from a snapshot. Overwrites the web app's current
        files and settings.
    text: >
        az webapp config snapshot restore -g MyResourceGroup -n MySite --time 2018-12-11T23:34:16.8388367
-   name: Restore a snapshot of web app SourceApp to web app TargetApp. Use --restore-content-only
        to not restore app settings. Overwrites TargetApp's files.
    text: >
        az webapp config snapshot restore -g TargetResourceGroup -n TargetApp --source-name
        SourceApp --source-resource-group OriginalResourceGroup --time 2018-12-11T23:34:16.8388367
        --restore-content-only
"""

helps["webapp config ssl"] = """
type: group
short-summary: Configure SSL certificates for web apps.
"""

helps["webapp config ssl bind"] = """
type: command
short-summary: Bind an SSL certificate to a web app.
examples:
-   name: Bind an SSL certificate to a web app.
    text: az webapp config ssl bind --ssl-type IP --resource-group MyResourceGroup
        --certificate-thumbprint {certificate-thumbprint} --name MyWebapp
    crafted: 'True'
-   name: Bind an SSL certificate to a web app.
    text: az webapp config ssl bind --ssl-type IP --resource-group MyResourceGroup
        --certificate-thumbprint {certificate-thumbprint} --name MyWebapp
    crafted: true
"""

helps["webapp config ssl delete"] = """
type: command
short-summary: Delete an SSL certificate from a web app.
examples:
-   name: Delete an SSL certificate from a web app.
    text: az webapp config ssl delete --certificate-thumbprint {certificate-thumbprint}
        --resource-group MyResourceGroup
    crafted: 'True'
-   name: Delete an SSL certificate from a web app.
    text: az webapp config ssl delete --certificate-thumbprint {certificate-thumbprint}
        --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp config ssl list"] = """
type: command
short-summary: List SSL certificates for a web app.
"""

helps["webapp config ssl unbind"] = """
type: command
short-summary: Unbind an SSL certificate from a web app.
"""

helps["webapp config ssl upload"] = """
type: command
short-summary: Upload an SSL certificate to a web app.
examples:
-   name: Upload an SSL certificate to a web app.
    text: az webapp config ssl upload --certificate-password {certificate-password}
        --query [0] --certificate-file {certificate-file} --resource-group MyResourceGroup
        --output json --name MyWebapp
    crafted: 'True'
-   name: Upload an SSL certificate to a web app.
    text: az webapp config ssl upload --certificate-password {certificate-password}
        --query [0] --certificate-file {certificate-file} --resource-group MyResourceGroup
        --output json --name MyWebapp
    crafted: true
"""

helps["webapp config storage-account"] = """
type: group
short-summary: Manage a web app's Azure storage account configurations. (Linux Web
    Apps and Windows Containers Web Apps Only)
"""

helps["webapp config storage-account add"] = """
type: command
short-summary: Add an Azure storage account configuration to a web app. (Linux Web
    Apps and Windows Containers Web Apps Only)
examples:
-   name: Add a connection to the Azure Files file share called MyShare in the storage
        account named MyStorageAccount.
    text: >
        az webapp config storage-account add -g MyResourceGroup -n MyUniqueApp \\
          --custom-id CustomId \\
          --type AzureFiles \\
          --account-name MyStorageAccount \\
          --share-name MyShare \\
          --access-key MyAccessKey \\
          --mount-path /path/to/mount
"""

helps["webapp config storage-account delete"] = """
type: command
short-summary: Delete a web app's Azure storage account configuration. (Linux Web
    Apps and Windows Containers Web Apps Only)
"""

helps["webapp config storage-account list"] = """
type: command
short-summary: Get a web app's Azure storage account configurations. (Linux Web Apps
    and Windows Containers Web Apps Only)
"""

helps["webapp config storage-account update"] = """
type: command
short-summary: Update an existing Azure storage account configuration on a web app.
    (Linux Web Apps and Windows Containers Web Apps Only)
examples:
-   name: Update the mount path for a connection to the Azure Files file share with
        the ID MyId.
    text: >
        az webapp config storage-account update -g MyResourceGroup -n MyUniqueApp
        \\
          --custom-id CustomId \\
          --mount-path /path/to/new/mount
"""

helps["webapp cors"] = """
type: group
short-summary: Manage Cross-Origin Resource Sharing (CORS)
"""

helps["webapp cors add"] = """
type: command
short-summary: Add allowed origins
examples:
-   name: add a new allowed origin
    text: >
        az webapp cors add -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
-   name: Add allowed origins.
    text: az webapp cors add --name {myAppName} --allowed-origins https://myapps.com
        --resource-group {myRG}
    crafted: 'True'
-   name: Add allowed origins.
    text: az webapp cors add --name {myAppName} --allowed-origins https://myapps.com
        --resource-group {myRG}
    crafted: true
"""

helps["webapp cors remove"] = """
type: command
short-summary: Remove allowed origins
examples:
-   name: remove an allowed origin
    text: >
        az webapp cors remove -g {myRG} -n {myAppName} --allowed-origins https://myapps.com
-   name: remove all allowed origins
    text: >
        az webapp cors remove -g {myRG} -n {myAppName} --allowed-origins *
-   name: Remove allowed origins.
    text: az webapp cors remove --name {myAppName} --allowed-origins https://myapps.com
        --resource-group {myRG}
    crafted: 'True'
-   name: Remove allowed origins.
    text: az webapp cors remove --name {myAppName} --allowed-origins https://myapps.com
        --resource-group {myRG}
    crafted: true
"""

helps["webapp cors show"] = """
type: command
short-summary: show allowed origins
"""

helps["webapp create"] = """
type: command
short-summary: Create a web app.
long-summary: The web app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
-   name: Create a web app with the default configuration.
    text: >
        az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName
-   name: Create a web app with a NodeJS 6.2 runtime and deployed from a local git
        repository.
    text: >
        az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName --runtime
        "node|6.2" --deployment-local-git
-   name: Create a web app.
    text: az webapp create --resource-group MyResourceGroup --plan MyPlan --name MyUniqueAppName
    crafted: 'True'
-   name: Create a web app.
    text: az webapp create --resource-group MyResourceGroup --plan MyPlan --name MyUniqueAppName
    crafted: true
"""

helps["webapp delete"] = """
type: command
short-summary: Delete a web app.
examples:
-   name: Delete a web app.
    text: az webapp delete --resource-group MyResourceGroup --name MyWebapp
    crafted: 'True'
-   name: Delete a web app.
    text: az webapp delete --resource-group MyResourceGroup --name MyWebapp
    crafted: true
"""

helps["webapp deleted"] = """
type: group
short-summary: Manage deleted web apps.
"""

helps["webapp deleted list"] = """
type: command
short-summary: List web apps that have been deleted.
"""

helps["webapp deleted restore"] = """
type: command
short-summary: Restore a deleted web app.
long-summary: Restores the files and settings of a deleted web app to the specified
    web app.
examples:
-   name: Restore a deleted app to the Staging slot of MySite.
    text: >
        az webapp deleted restore -g MyResourceGroup -n MySite -s Staging --deleted-id
        /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Web/deletedSites/1234
-   name: Restore a deleted app to the app MySite. Do not restore the deleted app's
        settings.
    text: >
        az webapp deleted restore -g MyResourceGroup -n MySite --deleted-id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Web/deletedSites/1234
        --restore-content-only
"""

helps["webapp deployment"] = """
type: group
short-summary: Manage web app deployments.
"""

helps["webapp deployment container"] = """
type: group
short-summary: Manage container-based continuous deployment.
"""

helps["webapp deployment container config"] = """
type: command
short-summary: Configure continuous deployment via containers.
examples:
-   name: Configure continuous deployment via containers.
    text: az webapp deployment container config --enable-cd false --resource-group
        MyResourceGroup --name MyWebapp
    crafted: 'True'
-   name: Configure continuous deployment via containers.
    text: az webapp deployment container config --enable-cd false --resource-group
        MyResourceGroup --name MyWebapp
    crafted: true
"""

helps["webapp deployment container show-cd-url"] = """
type: command
short-summary: Get the URL which can be used to configure webhooks for continuous
    deployment.
"""

helps["webapp deployment list-publishing-profiles"] = """
type: command
short-summary: Get the details for available web app deployment profiles.
examples:
-   name: Get the details for available web app deployment profiles.
    text: az webapp deployment list-publishing-profiles --output json --resource-group
        MyResourceGroup --query [0] --name MyWebapp
    crafted: 'True'
-   name: Get the details for available web app deployment profiles.
    text: az webapp deployment list-publishing-profiles --output json --resource-group
        MyResourceGroup --query [0] --name MyWebapp
    crafted: true
"""

helps["webapp deployment slot"] = """
type: group
short-summary: Manage web app deployment slots.
"""

helps["webapp deployment slot auto-swap"] = """
type: command
short-summary: Configure deployment slot auto swap.
"""

helps["webapp deployment slot create"] = """
type: command
short-summary: Create a deployment slot.
examples:
-   name: Create a deployment slot.
    text: az webapp deployment slot create --slot {slot} --resource-group MyResourceGroup
        --name MyWebapp
    crafted: 'True'
-   name: Create a deployment slot.
    text: az webapp deployment slot create --slot {slot} --resource-group MyResourceGroup
        --name MyWebapp
    crafted: true
"""

helps["webapp deployment slot delete"] = """
type: command
short-summary: Delete a deployment slot.
"""

helps["webapp deployment slot list"] = """
type: command
short-summary: List all deployment slots.
examples:
-   name: List all deployment slots.
    text: az webapp deployment slot list --resource-group MyResourceGroup --name MyWebapp
    crafted: 'True'
-   name: List all deployment slots.
    text: az webapp deployment slot list --resource-group MyResourceGroup --name MyWebapp
    crafted: true
"""

helps["webapp deployment slot swap"] = """
type: command
short-summary: Change deployment slots for a web app.
examples:
-   name: Swap a staging slot into production for the MyUniqueApp web app.
    text: >
        az webapp deployment slot swap  -g MyResourceGroup -n MyUniqueApp --slot staging     --target-slot
        production
-   name: Change deployment slots for a web app.
    text: az webapp deployment slot swap --target-slot {target-slot} --slot {slot}
        --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Change deployment slots for a web app.
    text: az webapp deployment slot swap --target-slot {target-slot} --slot {slot}
        --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp deployment source"] = """
type: group
short-summary: Manage web app deployment via source control.
"""

helps["webapp deployment source config"] = """
type: command
short-summary: Manage deployment from git or Mercurial repositories.
"""

helps["webapp deployment source config-local-git"] = """
type: command
short-summary: Get a URL for a git repository endpoint to clone and push to for web
    app deployment.
examples:
-   name: Get an endpoint and add it as a git remote.
    text: >
        az webapp deployment source config-local-git     -g MyResourceGroup -n MyUniqueApp


        git remote add azure     https://{deploy_user_name}@MyUniqueApp.scm.azurewebsites.net/MyUniqueApp.git
-   name: Get a URL for a git repository endpoint to clone and push to for web app
        deployment.
    text: az webapp deployment source config-local-git --resource-group MyResourceGroup
        --name MyWebapp
    crafted: 'True'
-   name: Get a URL for a git repository endpoint to clone and push to for web app
        deployment.
    text: az webapp deployment source config-local-git --resource-group MyResourceGroup
        --name MyWebapp
    crafted: true
"""

helps["webapp deployment source config-zip"] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a webapp.
long-summary: >
    By default Kudu assumes that zip deployments do not require any build-related
    actions like
    npm install or dotnet publish. This can be overridden by including a .deployment
    file in your
    zip file with the following content '[config] SCM_DO_BUILD_DURING_DEPLOYMENT =
    true',
    to enable Kudu detection logic and build script generation process.
    See https://github.com/projectkudu/kudu/wiki/Configurable-settings#enabledisable-build-actions-preview.
    Alternately the setting can be enabled using the az webapp config appsettings
    set command.
examples:
-   name: Perform deployment by using zip file content.
    text: >
        az webapp deployment source config-zip     -g {myRG} -n {myAppName}     --src
        {zip file path location}
-   name: Perform deployment using the kudu zip push deployment for a webapp.
    text: az webapp deployment source config-zip --src {src} --name MyWebapp --resource-group
        MyResourceGroup
    crafted: 'True'
-   name: Perform deployment using the kudu zip push deployment for a webapp.
    text: az webapp deployment source config-zip --src {src} --name MyWebapp --resource-group
        MyResourceGroup
    crafted: true
"""

helps["webapp deployment source delete"] = """
type: command
short-summary: Delete a source control deployment configuration.
"""

helps["webapp deployment source show"] = """
type: command
short-summary: Get the details of a source control deployment configuration.
"""

helps["webapp deployment source sync"] = """
type: command
short-summary: Synchronize from the repository. Only needed under manual integration
    mode.
"""

helps["webapp deployment user"] = """
type: group
short-summary: Manage user credentials for deployment.
"""

helps["webapp deployment user set"] = """
type: command
short-summary: Update deployment credentials.
long-summary: All function and web apps in the subscription will be impacted since
    they share the same deployment credentials.
examples:
-   name: Set FTP and git deployment credentials for all apps.
    text: >
        az webapp deployment user set --user-name MyUserName
-   name: Update deployment credentials.
    text: az webapp deployment user set --user-name MyUserName --password {password}
    crafted: 'True'
-   name: Update deployment credentials.
    text: az webapp deployment user set --user-name MyUserName --password {password}
    crafted: true
"""

helps["webapp identity"] = """
type: group
short-summary: manage webapp's managed service identity
"""

helps["webapp identity assign"] = """
type: command
short-summary: assign or disable managed service identity to the webapp
examples:
-   name: assign local identity and assign a reader role to the current resource group.
    text: >
        az webapp identity assign -g MyResourceGroup -n MyUniqueApp --role reader
        --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/MyResourceGroup
-   name: enable identity for the webapp.
    text: >
        az webapp identity assign -g MyResourceGroup -n MyUniqueApp
-   name: Assign or disable managed service identity to the webapp.
    text: az webapp identity assign --resource-group MyResourceGroup --name MyUniqueApp
    crafted: 'True'
-   name: Assign or disable managed service identity to the webapp.
    text: az webapp identity assign --resource-group MyResourceGroup --name MyUniqueApp
    crafted: true
"""

helps["webapp identity remove"] = """
type: command
short-summary: Disable webapp's managed service identity
"""

helps["webapp identity show"] = """
type: command
short-summary: display webapp's managed service identity
examples:
-   name: Display webapp's managed service identity.
    text: az webapp identity show --output json --name MyWebapp --query [0] --resource-group
        MyResourceGroup
    crafted: 'True'
-   name: Display webapp's managed service identity.
    text: az webapp identity show --output json --name MyWebapp --query [0] --resource-group
        MyResourceGroup
    crafted: true
"""

helps["webapp list"] = """
type: command
short-summary: List web apps.
examples:
-   name: List default host name and state for all web apps.
    text: >
        az webapp list --query "[].{hostName: defaultHostName, state: state}"
-   name: List all running web apps.
    text: >
        az webapp list --query "[?state=='Running']"
"""

helps["webapp list-runtimes"] = """
type: command
short-summary: List available built-in stacks which can be used for web apps.
"""

helps["webapp log"] = """
type: group
short-summary: Manage web app logs.
"""

helps["webapp log config"] = """
type: command
short-summary: Configure logging for a web app.
examples:
-   name: Configure logging for a web app.
    text: az webapp log config --web-server-logging filesystem --resource-group MyResourceGroup
        --name MyWebapp
    crafted: 'True'
-   name: Configure logging for a web app.
    text: az webapp log config --web-server-logging filesystem --resource-group MyResourceGroup
        --name MyWebapp
    crafted: true
"""

helps["webapp log download"] = """
type: command
short-summary: Download a web app's log history as a zip file.
long-summary: This command may not work with web apps running on Linux.
examples:
-   name: Download a web app's log history as a zip file.
    text: az webapp log download --slot {slot} --resource-group MyResourceGroup --log-file
        {log-file} --name MyWebapp
    crafted: 'True'
-   name: Download a web app's log history as a zip file.
    text: az webapp log download --slot {slot} --resource-group MyResourceGroup --log-file
        {log-file} --name MyWebapp
    crafted: true
"""

helps["webapp log show"] = """
type: command
short-summary: Get the details of a web app's logging configuration.
"""

helps["webapp log tail"] = """
type: command
short-summary: Start live log tracing for a web app.
long-summary: This command may not work with web apps running on Linux.
examples:
-   name: Start live log tracing for a web app.
    text: az webapp log tail --resource-group MyResourceGroup --name MyWebapp
    crafted: 'True'
-   name: Start live log tracing for a web app.
    text: az webapp log tail --resource-group MyResourceGroup --name MyWebapp
    crafted: true
"""

helps["webapp restart"] = """
type: command
short-summary: Restart a web app.
examples:
-   name: Restart a web app.
    text: az webapp restart --resource-group MyResourceGroup --name MyWebapp
    crafted: 'True'
-   name: Restart a web app.
    text: az webapp restart --resource-group MyResourceGroup --name MyWebapp
    crafted: true
"""

helps["webapp show"] = """
type: command
short-summary: Get the details of a web app.
examples:
-   name: Get the details of a web app.
    text: az webapp show --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Get the details of a web app.
    text: az webapp show --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp ssh"] = """
type: command
short-summary: (Preview) SSH command establishes a ssh session to the web container
    and developer would get a shell terminal remotely.
examples:
-   name: ssh into a webapp
    text: >
        az webapp ssh -n MyUniqueAppName -g MyResourceGroup
"""

helps["webapp start"] = """
type: command
short-summary: Start a web app.
examples:
-   name: Start a web app.
    text: az webapp start --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Start a web app.
    text: az webapp start --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp stop"] = """
type: command
short-summary: Stop a web app.
examples:
-   name: Stop a web app.
    text: az webapp stop --name MyWebapp --resource-group MyResourceGroup
    crafted: 'True'
-   name: Stop a web app.
    text: az webapp stop --name MyWebapp --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp traffic-routing"] = """
type: group
short-summary: Manage traffic routing for web apps.
"""

helps["webapp traffic-routing clear"] = """
type: command
short-summary: Clear the routing rules and send all traffic to production.
"""

helps["webapp traffic-routing set"] = """
type: command
short-summary: Configure routing traffic to deployment slots.
"""

helps["webapp traffic-routing show"] = """
type: command
short-summary: Display the current distribution of traffic across slots.
"""

helps["webapp up"] = """
type: command
short-summary: (Preview) Create and deploy existing local code to the webapp, by running
    the command from the folder where the code is present. Supports running the command
    in preview mode using --dryrun parameter. Current supports includes Node, Python,.NET
    Core, ASP.NET, staticHtml. Node, Python apps are created as Linux apps. .Net Core,
    ASP.NET and static HTML apps are created as Windows apps. If command is run from
    an empty folder, an empty windows webapp is created.
examples:
-   name: View the details of the app that will be created, without actually running
        the operation
    text: >
        az webapp up -n MyUniqueAppName --dryrun
-   name: Create a web app with the default configuration, by running the command
        from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName
-   name: Create a web app in a sepcific region, by running the command from the folder
        where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName -l locationName
-   name: Deploy new code to an app that was originally created using the same command
    text: >
        az webapp up -n MyUniqueAppName -l locationName
-   name: Experimental command to create and deploy a web app. Current supports includes
        Node, Python on Linux & .NET Core, ASP.NET, staticHtml on Windows.
    text: az webapp up --name MyWebapp
    crafted: 'True'
-   name: Experimental command to create and deploy a web app. Current supports includes
        Node, Python on Linux & .NET Core, ASP.NET, staticHtml on Windows.
    text: az webapp up --name MyWebapp
    crafted: true
"""

helps["webapp update"] = """
type: command
short-summary: Update a web app.
examples:
-   name: Update the tags of a web app.
    text: >
        az webapp update -g MyResourceGroup -n MyAppName --set tags.tagName=tagValue
-   name: Update a web app.
    text: az webapp update --https-only false --name MyAppName --resource-group MyResourceGroup
    crafted: 'True'
-   name: Update a web app.
    text: az webapp update --https-only false --name MyAppName --resource-group MyResourceGroup
    crafted: true
"""

helps["webapp webjob"] = """
type: group
short-summary: Allows management operations for webjobs on a webapp.
"""

helps["webapp webjob continuous"] = """
type: group
short-summary: Allows management operations of continuous webjobs on a webapp.
"""

helps["webapp webjob continuous list"] = """
type: command
short-summary: List all continuous webjobs on a selected webapp.
examples:
-   name: List all continuous webjobs on a selected webapp.
    text: az webapp webjob continuous list --resource-group MyResourceGroup --name
        MyWebapp
    crafted: 'True'
-   name: List all continuous webjobs on a selected webapp.
    text: az webapp webjob continuous list --resource-group MyResourceGroup --name
        MyWebapp
    crafted: true
"""

helps["webapp webjob continuous remove"] = """
type: command
short-summary: Delete a specific continuous webjob.
"""

helps["webapp webjob continuous start"] = """
type: command
short-summary: Start a specific continuous webjob on a selected webapp.
"""

helps["webapp webjob continuous stop"] = """
type: command
short-summary: Stop a specific continuous webjob.
"""

helps["webapp webjob triggered"] = """
type: group
short-summary: Allows management operations of triggered webjobs on a webapp.
"""

helps["webapp webjob triggered list"] = """
type: command
short-summary: List all triggered webjobs hosted on a webapp.
"""

helps["webapp webjob triggered log"] = """
type: command
short-summary: Get history of a specific triggered webjob hosted on a webapp.
"""

helps["webapp webjob triggered remove"] = """
type: command
short-summary: Delete a specific triggered webjob hosted on a webapp.
"""

helps["webapp webjob triggered run"] = """
type: command
short-summary: Run a specific triggered webjob hosted on a webapp.
"""