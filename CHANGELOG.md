# Release 2025.2 (2025-07-04)

## General changes

### Improvements

- Use the GET /api/v2/health API endpoint in the health check of the docker container

### Upgrade notes

- Please follow the documented [upgrade procedure](https://docs.inmanta.com/community/latest/administrators/upgrading_the_orchestrator.html)
- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 16.0.0 (2025-07-04)

### New features

- Implemented a GraphQL endpoint. Added a query to fetch environments that supports filtering, sorting and paging. ([#8736](https://github.com/inmanta/inmanta-core/issues/8736))
- Added support for dataclasses in plugins.. See [plugins](module-plugins)
- Added support for secrets and references in inmanta models. For more information, [see documentation](references)

### Improvements

- Added documentation about unknowns ([#6056](https://github.com/inmanta/inmanta-core/issues/6056))
- Added support to build sdist of V2 module. ([inmanta/inmanta-core#8111](https://github.com/inmanta/inmanta-core/issues/8111))
- Add support for native python types in plugins. Plugin developers can now use mypy on inmanta plugins. Union types are now supported as typing annotations in plugins.
For more information, please refer to the [plugins](module-plugins) documentation.
 ([#8577](https://github.com/inmanta/inmanta-core/issues/8577))
- The scheduler and the compiler no longer connect to the server using the `server.bind-address` instead they always use localhost. ([inmanta/inmanta-core#8752](https://github.com/inmanta/inmanta-core/issues/8752))
- Improve the logging of code loading failures during resource deployment.
- For partial compile, allow resources to move between resource sets if both sets are being updated ([#9042](https://github.com/inmanta/inmanta-core/issues/9042))
- Add support for references in dicts or lists in references ([#9220](https://github.com/inmanta/inmanta-core/issues/9220))
- Added the 'GET /api/v2/health' endpoint.
- Compiler: support inheritance for dataclass entities. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Remove v1 module from getting started documentation
- Add released field to /api/v2/desiredstate
- Improve error message on login endpoint about invalid credentials.
- Vendored pyformance to fix warning about pkg_resources being deprecated ([#9235](https://github.com/inmanta/inmanta-core/issues/9235))
- Compiler: added the ``inmanta.plugins.allow_reference_values`` function to explicitly allow access to reference values by traversing the model from a plugin. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Compiler: allow references in dict attributes. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Added default equals implementation to references
- Log a clear error message if a Resource accidentally inherits from the resource decorator instead of the Resource class. ([inmanta/inmanta-core#8817](https://github.com/inmanta/inmanta-core/issues/8817))
- Added support for bearer token based auth in openapi documentation.
- Added support to provide the access token of the `GET /api/v2/docs` endpoint via the `token` query parameter instead of via the Authorization header.
- Mark parameters in the path of an endpoint using `<param>` instead of `{param}` in the openapi documentation.

### Known Issues

- References are currently not supported inside a resource's list attributes.

### Upgrade notes

- Removed the `POST /api/v1/agent/<id>` API endpoint.
- Agents will now only attempt to deploy resources if they encountered no errors during code loading. ([#9259](https://github.com/inmanta/inmanta-core/issues/9259))
- Access control using claim match expressions in no longer supported.

### Deprecation notes

- Removed the resource_action_update endpoint

### Bug fixes

- Make the `get_scheduler_status` endpoint return a 404 if the scheduler is not running. ([inmanta/inmanta-core#8516](https://github.com/inmanta/inmanta-core/issues/8516))
- Fixed bug that caused code loading problems not to be reported into the resource action log. ([inmanta/inmanta-core#8722](https://github.com/inmanta/inmanta-core/issues/8722))
- Fix issue where empty versions are not correctly passed to the scheduler ([#8799](https://github.com/inmanta/inmanta-core/issues/8799))
- Fix pydantic deprecation warning at startup ([#8921](https://github.com/inmanta/inmanta-core/issues/8921))
- Fix bug where the POST /api/v2/environment_auth endpoint returns a 400 if the server.auth=true config option was set using an environment variable. ([inmanta/inmanta-core#8962](https://github.com/inmanta/inmanta-core/issues/8962))
- Fix bug where the scheduler is paused by calling the `POST /api/v2/agents/pause` endpoint. ([inmanta/inmanta-core#9081](https://github.com/inmanta/inmanta-core/issues/9081))
- Compiler: fixed bug where compiler would crash under specific circumstances on calling a plugin that takes a union involving a dataclass as parameter. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Only report the desired state as active when the new version is loaded by the scheduler
- Updated the return type of HandlerAPI.facts from dict[str, object] to dict[str, str] for consistency with HandlerContext.set_dact
- Fix bug where configuration options with a dot in their section name could not be read from an environment variable. ([inmanta/inmanta-lsm#1995](https://github.com/inmanta/inmanta-lsm/issues/1995))
- Fixed bug that can cause the Python environment of a executor to be shared across different Inmanta environment. This could result in a corrupt executor environment.
- Compiler: improved clarity of error reporting related to references. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Compiler: implemented more thorough checks for references passed into plugins, and accessed by traversing the model from plugins, so they don't show up where they may not be expected. For more details, see the [documentation](references). ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Compiler: reference values passed into or accessed from plugins, when explicitly declared, are now passed as proper ``Reference`` objects instead of being wrapped in a ``DynamicProxy``. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Compiler: made sure f-strings and old-style string format expressions raise a clear error when attempting to substitute a reference value. ([#8946](https://github.com/inmanta/inmanta-core/issues/8946))
- Make sure dry-runs load the appropriate handler code for their version
- Fix bug where starting the agent can result in an error saying that stdout_log is referenced before assignment. This can cause the compiler service to get stuck or trigger the agent deploy timers at incorrect moments. ([inmanta/inmanta-core#9275](https://github.com/inmanta/inmanta-core/issues/9275))

### Other notes

- Adds the following consts to the stable api:
  - UNDEPLOYABLE_STATES
  - TRANSIENT_STATES
  - NOT_DONE_STATES
  - DONE_STATES

- Removed resource events and logs when resources are marked as undefined or skipped_for_undefined
and when they are marked as deployed due to known good status


## Inmanta-ui: release 5.1.7 (2025-07-04)

### Bug fixes

- Make sure the index.html and config.js file is not cached by the browser.
- Make sure that requests for `/console/version.json` are not cached by the browser.


## Inmanta-ui: release 5.1.6 (2025-04-08)

No changelog entries.

## Web-console: release 3.0.0 (2025-07-04)

### New features

- Replace the collapsible sections in the compile details page with a log viewer. ([#6061](https://github.com/inmanta/web-console/issues/6061))
- Implementation of a markdown previewer for the instance documentation. ([#6268](https://github.com/inmanta/web-console/issues/6268))

### Improvements

- Replace old modals implementation with Global modal implementation. ([#6130](https://github.com/inmanta/web-console/issues/6130))
- Replace old Login page implementation with Patternfly Login page. Repair redirects to login page and cover trailing slashes in routes. ([#6131](https://github.com/inmanta/web-console/issues/6131))
- Improve itemization in Firefox for the status page. ([#6183](https://github.com/inmanta/web-console/issues/6183))
- Add a way to copy the markdown with escaped newlines. ([#6268](https://github.com/inmanta/web-console/issues/6268))
- Increase the default page size for the Resources page. ([#6277](https://github.com/inmanta/web-console/issues/6277))
- Add the query factory to improve the maintenance of the communication with backend. ([#6318](https://github.com/inmanta/web-console/issues/6318))
- improve inline edit error handling ([#6330](https://github.com/inmanta/web-console/issues/6330))
- Improve build checks in Jest to fail tests on console.error and console.warn. ([#6347](https://github.com/inmanta/web-console/issues/6347))
- Remove the old codeHighlighter and replace it with the new CodeEditor component. ([#6359](https://github.com/inmanta/web-console/issues/6359))
- Include the Json-bigint package in the project. ([#6379](https://github.com/inmanta/web-console/issues/6379))
- Improve the halting and resuming of environments between the browser tabs ([#6400](https://github.com/inmanta/web-console/issues/6400))
- Add option to change user password in the user management page ([#6439](https://github.com/inmanta/web-console/issues/6439))
- Add padding on the right side of the documentation tab to avoid content being overlapped by scrollbar ([#6441](https://github.com/inmanta/web-console/issues/6441))
- Improve display of errors in the Instance Composer and Compile Details

### Bug fixes

- Fix styling of disabled submit button in the service instance form ([#6237](https://github.com/inmanta/web-console/issues/6237))
- Allow deleting embedded entities when the minimum is not reached. ([#6333](https://github.com/inmanta/web-console/issues/6333))
- Enable authentication on documentation links. ([#6335](https://github.com/inmanta/web-console/issues/6335))
- Generate links for resource IDs using regex, regardless of the version suffix being present or not. ([#6371](https://github.com/inmanta/web-console/issues/6371))
- Fix the issue where dragging from stencil sidebar in instance composer inter-service relations was not working as expected.
- Enforce clearing the cookies when the user is not authenticated.


## Web-console: release 2.1.1 (2025-04-09)

### Improvements

- Implement darkmode. The user can now enable darkmode in the top right menu. ([#5109](https://github.com/inmanta/web-console/issues/5109))
- Add the correct name for embedded entities as it's now available in the service model ([#5591](https://github.com/inmanta/web-console/issues/5591))
- REplace service queries for react Query ([#5975](https://github.com/inmanta/web-console/issues/5975))
- Change default search in then service inventory to Id ([#5983](https://github.com/inmanta/web-console/issues/5983))
- extracted error messages from the JSON-editor and Instance composer to reduce code duplication ([#6059](https://github.com/inmanta/web-console/issues/6059))
- Improve casing of names of instance groups in Instance Composer ([#6155](https://github.com/inmanta/web-console/issues/6155))
- Improve Query Management for service and service instance queries with replacement of v1 queries with react-query implementation ([#6174](https://github.com/inmanta/web-console/issues/6174))
- Improve Query Management with removal of duplicate implmentation of react query, now we use reusable hooks to manage queries, headers and base error handling ([#6178](https://github.com/inmanta/web-console/issues/6178))
- Prevent stretched buttons in header, and enable token tab in the settings for jwt auth. ([#6215](https://github.com/inmanta/web-console/issues/6215))
- Added V2 query managers for compilation-related features and fixed test assertions in ContinuousWithEnv tests. ([#6223](https://github.com/inmanta/web-console/issues/6223))
- Upgrade support for mermaid v11 diagrams and enable zooming on svg files in the documentation. ([#6258](https://github.com/inmanta/web-console/issues/6258))
- Improve overal navigation through the application. ([#5950](https://github.com/inmanta/web-console/issues/5950))

### Bug fixes

- Resolved the issue of cells overlapping in the instance composer ([#6154](https://github.com/inmanta/web-console/issues/6154))
- Fix handling of rw fields in Instance Composer when in edit mode ([#6176](https://github.com/inmanta/web-console/issues/6176))
- Fix lack of visibility of default filter for desired state page ([#6206](https://github.com/inmanta/web-console/issues/6206))
- Fix wrong conversion between JSON editor and regular form ([#6177](https://github.com/inmanta/web-console/issues/6177))
- Fix bug with visibility of nested fields in input where they are set to null ([#6252](https://github.com/inmanta/web-console/issues/6252))


# Release 2025.1.1 (2025-05-27)

## Upgrade notes

- Please follow the documented [upgrade procedure](https://docs.inmanta.com/community/latest/administrators/upgrading_the_orchestrator.html)
- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 15.0.1 (2025-05-27)

### Other notes

- Bump tornado version to 6.5.1 (CVE-2025-47287)

## inmanta-ui: release 5.1.5
This component has had no new releases since the last product version.
## web-console: release 2.1.0
This component has had no new releases since the last product version.


# Release 2025.1 (2025-01-17)

## General changes

### New features

- Update python lower bound to 3.12 for ISO8

### Upgrade notes

- The image inmanta/orchestrator:2025.1 introduces a number of changes, including these breaking changes:
  - Server options --wait-for-host and --wait-for-port are deprecated and will be ignored.
  - Providing environment variables in /etc/inmanta/env is not supported anymore.
 ([inmanta/inmanta-core#8304](https://github.com/inmanta/inmanta-core/issues/8304))
- Supported PostgreSQL version is now version 16. ([inmanta/inmanta-core#8464](https://github.com/inmanta/inmanta-core/issues/8464))
- The orchestrator docker image now writes the Inmanta server logs to both stdout and to /var/log/inmanta/server.log by default. ([inmanta/inmanta-service-orchestrator#527](https://github.com/inmanta/inmanta-service-orchestrator/issues/527))
- The legacy, RPM based container is no longer available, switch to the native container instead
- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 15.0.0 (2025-01-17)

### New features

- Added SkipResourceForDependencies exception. This exception can be raised by the handler when it wants to skip a resource and retry only when all of its dependencies succeed. See the {py:class}`inmanta.agent.handler.SkipResourceForDependencies` for more details.
 ([#8340](https://github.com/inmanta/inmanta-core/issues/8340))
- Added support for fine grained customization of log configuration, see [logging documentation](administrators_doc_logging).
- Added support for python types in plugin annotations

### Improvements

- Redesign the server on-disk layout. The server will now store its state in the ``<state-dir>/server`` directory.

- Make compiler venv have the python version in the name ([#7732](https://github.com/inmanta/inmanta-core/issues/7732))
- Update database pool status reporting for the new scheduler ([#8228](https://github.com/inmanta/inmanta-core/issues/8228))
- Add support for per-component log file ([#8306](https://github.com/inmanta/inmanta-core/issues/8306))
- Add API endpoint for scheduler self-check ([#8321](https://github.com/inmanta/inmanta-core/issues/8321))
- Improve the performance of the increment calculation.
- Added MultiLineFormatter to the stable api

### Upgrade notes

- The on-disk layout of the server has been changed. After upgrade, old files can be cleaned up with the following commands:
  - old environment files: `rm -rf /var/lib/inmanta/server/environments/`
  - old agent config files: `rm -rf /var/lib/inmanta/server/agents/`
  - old agent work folders (all folders formatted as uuids): `find /var/lib/inmanta -maxdepth 1 -regextype grep -regex '.*/[a-f0-9]\{8\}-[a-f0-9]\{4\}-[a-f0-9]\{4\}-[a-f0-9]\{4\}-[a-f0-9]\{12\}' -type d -delete`

- Add support for periodic per-resource deploys and repairs. When ``AUTOSTART_AGENT_REPAIR_INTERVAL``  or ``AUTOSTART_AGENT_DEPLOY_INTERVAL`` are specified as a number (not a cron expression), they are interpreted on a per-resource basis. The timer will trigger after the interval has expired, after the last deploy of each individual resource.

- Previously, a single database connection pool was configured
via the [database.connection-pool-max-size](#database.connection-pool-max-size) and [database.connection-pool-min-size](#database.connection-pool-min-size) options.
Now, the new resource scheduler uses an additional database connection pool per environment.
Please review the following connection pool options and make sure they fit your
needs. Do keep in mind that these options will apply to all active environments:
  - For the server: [server.db-connection-pool-max-size](#server.db-connection-pool-max-size), [server.db-connection-pool-min-size](#server.db-connection-pool-min-size), [server.db-connection-timeout](#server.db-connection-timeout).
    By default, the server pool will be 50% the size of the previous global pool.
  - For the scheduler: [scheduler.db-connection-pool-max-size](#scheduler.db-connection-pool-max-size), [scheduler.db-connection-pool-min-size](#scheduler.db-connection-pool-min-size), [scheduler.db-connection-timeout](#scheduler.db-connection-timeout).
    By default, each scheduler pool will be 10% the size of the previous global pool.
These defaults are tuned to 5 environments per server, if you have more or fewer, please adjust accordingly.
 ([#8193](https://github.com/inmanta/inmanta-core/issues/8193))
- All api endpoints reporting deployment status for specific versions of resources have been removed.

| api endpoint | change | alternative |
| ------------ | ------ | ------------|
| `/api/v1/resource/<id>` | removal of the status argument and removal of status field from the response | `/api/v2/resource/<id>/` |
| `/api/v1/version/<id>` | removal of `resources/status` field from the response | `/api/v2/resource` |
 ([#8196](https://github.com/inmanta/inmanta-core/issues/8196))
- The deployment status can only be correctly determined for the current moment.
For this reason the ``deployed`` and ``status`` field has been removed for all but the latest active version.

| api endpoint | change | alternative |
| ------------ | ------ | ------------|
| `GET /api/v1/version` | removal of the `deployed` and `result` fields from the response | `GET /api/v2/resource/` |
| `GET /api/v1/version/<id>` | removal of the `deployed` and `result` fields from the response | `GET /api/v2/resource` |
| `POST /api/v1/version/<id>` | removal of the `deployed` and `result` fields from the response |  `GET /api/v2/resource` |

| command | change |
|---------| ------ |
| `inmanta-cli version release` | removal of the "Deployed" and "# Done" columns from the output and "State" field now reports the same state as the corresponding page in the web-console |
| `inmanta-cli version list` | removal of the "Deployed" and "# Done" columns from the output and "State" field now reports the same state as the corresponding page in the web-console |
 ([#8252](https://github.com/inmanta/inmanta-core/issues/8252))
- Removed the `inmanta deploy` command. ([inmanta/inmanta-core#8612](https://github.com/inmanta/inmanta-core/issues/8612))
- The agent splay environment settings have been removed. Due to per-resource repair and deploy timers, splaying is no longer required ([#8619](https://github.com/inmanta/inmanta-core/issues/8619))
- The lowest supported python version was increased to 3.12 ([#8315](https://github.com/inmanta/inmanta-core/issues/8315))

### Deprecation notes

- Remove deprecated `inmanta module commit` command. Please use the `inmanta module release` command instead to perform a release for a module.
 ([inmanta/irt#1597](https://github.com/inmanta/irt/issues/1597))
- The `//` syntax for comments is no longer supported. Please use `#` for comments.
 ([#6972](https://github.com/inmanta/inmanta-core/issues/6972))
- The following configuration options were removed:
  - config.agent-map
  - config.use_autostart_agent_map
  - config.agent-names
  - config.agent-get-resource-backoff
  - unknown_handler.default
  - server.auto-recompile-wait
  - config.agent-interval
  - config.agent-splay
  - server_rest_transport.port

The following environment settings were removed:
  - push_on_auto_deploy
  - agent_trigger_method_on_auto_deploy
  - environment_agent_trigger_method
  - autostart_agent_map
  - autostart_agent_deploy_splay
  - autostart_agent_repair_splay

The following internal API endpoints were removed:
  - get_resources_for_agent: `GET /api/v1/resource`
  - get_code: `GET api/v1/code/<id>`
  - resource_event: `PUT api/v1/event/<id>`
  - update_agent_map: `POST api/v2/agentmap`
  - resource_deploy_done: `POST api/v2/resource/<rvid>/deploy/done`
  - resource_deploy_start: `POST api/v2/resource/<rvid>/deploy/start`

The following settings are being deprecated:
  - [database.connection-pool-max-size](#database.connection-pool-max-size) replaced by [server.db-connection-pool-max-size](#server.db-connection-pool-max-size) and [scheduler.db-connection-pool-max-size](#scheduler.db-connection-pool-max-size).
  - [database.connection-pool-min-size](#database.connection-pool-min-size) replaced by [server.db-connection-pool-min-size](#server.db-connection-pool-min-size) and [scheduler.db-connection-pool-min-size](#scheduler.db-connection-pool-min-size).
  - [database.connection-timeout](#database.connection-timeout) replaced by [server.db-connection-timeout](#server.db-connection-timeout) and [scheduler.db-connection-timeout](#scheduler.db-connection-timeout).
 ([inmanta/inmanta-core#8197](https://github.com/inmanta/inmanta-core/issues/8197))
- Dropped deprecated methods `set_log_level`, `set_log_formatter`, `set_logfile_location` and `get_handler` from `inmanta.logging.InmantaLoggerConfig`. Use the `apply_options` method or a log config file instead.
 ([#8485](https://github.com/inmanta/inmanta-core/issues/8485))

### Bug fixes

- Fixed pagination metadata when on a page behind the last result, or before the first result (due to filtering) ([#7898](https://github.com/inmanta/inmanta-core/issues/7898))
- Fix handling of extras in legacy dependency check ([#8405](https://github.com/inmanta/inmanta-core/issues/8405))
- Don't refresh facts that no longer exist in the latest released model version. ([inmanta/inmanta-core#8456](https://github.com/inmanta/inmanta-core/issues/8456))
- Fix the typing of agent cache and plugins decorators.
- Fix clearing of increment cache on environment delete

## Inmanta-ui: release 5.1.5 (2025-01-17)

No changelog entries.

## Web-console: release 2.1.0 (2025-01-17)

### New features

- Complete redesign of the Instance Composer, main focus was to align its general functionalities with regular form, and improve the user experience. This change includes: A right sidebar, to have better access to the form fields of different parts of the instance A left sidebar, from which we can drag and drop embedded entities and existing Inter-Service Relations from the inventory. Inter-Service Relations can only be edited when opened individualy in the Instance Composer. Zooming can now be done with a slider, and two new functionalities have been added. Zoom-to-fit and full-screen mode. ([#5868](https://github.com/inmanta/web-console/issues/5868))

### Improvements

- Implement the Events tab on the Instance details page. ([#5781](https://github.com/inmanta/web-console/issues/5781))
- Implement the Resource tab on the Instance details page. ([#5782](https://github.com/inmanta/web-console/issues/5782))
- Add navigation button to Diagnose view from instance details page, add ability to adjust look back property for the diagnose ([#5842](https://github.com/inmanta/web-console/issues/5842))
- Add a feedback component to the composer to provide user with information about the missing required inter-service relations ([#5870](https://github.com/inmanta/web-console/issues/5870))
- Simplify the documentation tab when there's only one item available. ([#5916](https://github.com/inmanta/web-console/issues/5916))
- Align all the input descriptions in the service instance forms ([#5921](https://github.com/inmanta/web-console/issues/5921))
- Add support for emoji to the Documentation Tab ([#5931](https://github.com/inmanta/web-console/issues/5931))
- Add button to disable expert mode from the banner ([#5942](https://github.com/inmanta/web-console/issues/5942))
- Adds discovery uri to the Discovered Resources Page ([#5946](https://github.com/inmanta/web-console/issues/5946))
- Add screen reader text for empty columns headers to improve accessibility ([#5949](https://github.com/inmanta/web-console/issues/5949))
- Emphasize terminated instances in the instance details view ([#5951](https://github.com/inmanta/web-console/issues/5951))
- Create a global modal component for use across the application, to improve performance and reduce code duplication. ([#5965](https://github.com/inmanta/web-console/issues/5965))
- Unify colors and fonts in the composer entity headers ([#5986](https://github.com/inmanta/web-console/issues/5986))
- Hide Left sidebar from the Instance Composer when in the view mode ([#5988](https://github.com/inmanta/web-console/issues/5988))
- Improve information messages in the form in the Instance Composer ([#5990](https://github.com/inmanta/web-console/issues/5990))
- Move action buttons to the page header, to improve spacing ([#5991](https://github.com/inmanta/web-console/issues/5991))
- Improve behavior of useEffects in the Instance Composer when related inventories are updated ([#5997](https://github.com/inmanta/web-console/issues/5997))
- Add highlighting for not connected inter-service relations elements on the canvas in the Instance Composer ([#5998](https://github.com/inmanta/web-console/issues/5998))
- Support nested status properties in the Status Page ([#6018](https://github.com/inmanta/web-console/issues/6018))
- Upgrade the Patternfly library to V6. ([#6025](https://github.com/inmanta/web-console/issues/6025))
- Add identifying attributes to pool of displayed attributes in the body of the composer entities ([#6031](https://github.com/inmanta/web-console/issues/6031))
- Hide read-only embedded entities from the Canvas in the Instance Composer to make the view cleaner ([#6034](https://github.com/inmanta/web-console/issues/6034))
- Change the buttons in the Composer Sidebar ([#6035](https://github.com/inmanta/web-console/issues/6035))
- Instance composer will render all required by default embedded entities in the canvas ([#6037](https://github.com/inmanta/web-console/issues/6037))
- Improve the display of timestamps in the instance details page. ([#6047](https://github.com/inmanta/web-console/issues/6047))
- Modify Service Details Page to use direct service instance data for latest version instead latest instance logs ([#6058](https://github.com/inmanta/web-console/issues/6058))
- Remove the collapsible functionality in the Service Inventory table. The new Instance Details page replaces the content of the collapsible sections. ([#6104](https://github.com/inmanta/web-console/issues/6104))
- Move progress bar form resource tab to details section ([#5782](https://github.com/inmanta/web-console/issues/5782))
- Fix spacing and font sizes in status page to improve UI and readability of the view ([#6120](https://github.com/inmanta/web-console/issues/6120))
- Fix slider display issue in firefox, fix rounding in the highlighter, fix fetching cache issue for composer initial load, fix overflow issue for text list field in composer ([#6124](https://github.com/inmanta/web-console/issues/6124))
- Move the option to go to the instance details into the row as primary action button. ([#6125](https://github.com/inmanta/web-console/issues/6125))
- Improve the Documentation tab on the Instance details page when only one documentation section is available. ([#6122](https://github.com/inmanta/web-console/issues/6122))
- Improve the tags for the versions on the instance details page. ([#6142](https://github.com/inmanta/web-console/issues/6142))
- Add Infinite query to History section ([#6150](https://github.com/inmanta/web-console/issues/6150))
- Align colors of labels and fix colors of progress bars

### Bug fixes

- Removing embedded entities in the form wasn't consistently removing the correct item. A unique identifier has been added to the form elements to ensure the correct item is removed. ([#5969](https://github.com/inmanta/web-console/issues/5969))
- Resolve issue when inter-service relation attribute value is set to null AutoCompleteInput crashes. ([#5993](https://github.com/inmanta/web-console/issues/5993))
- Fix issue with missing inter-service relations on the canvas ([#6030](https://github.com/inmanta/web-console/issues/6030))
- Fix issue when toggling embedded entities of the same type in the instance composer ([#6138](https://github.com/inmanta/web-console/issues/6138))


# Release 2024.4 (2024-10-10)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 14.0.0 (2024-10-10)

### New features

- Added a 'receive_events' attribute to resources. It allows you to control which resources get events from their dependencies, i.e. wether or not they need to be redeployed after a dependency deploys. See the `std::Resource` documentation for more details. ([#8012](https://github.com/inmanta/inmanta-core/issues/8012))
- Removed built-in io in favor of the more flexible mitogen module.
- Added telemetry support for tracing calls through the orchestrator.

### Improvements

- Include the documentation of modules composing a product into the documentation of the product when they contain a README.md file.
 ([inmanta/irt#2026](https://github.com/inmanta/irt/issues/2026))
- Update the endpoints returning discovered resource (`GET /api/v2/discovered/<discovered_resource_id>` and `GET /api/v2/discovered`) to include a link to the resource responsible for the discovery.
 ([#7528](https://github.com/inmanta/inmanta-core/issues/7528))
- Provide the exception that caused a resource load to fail in the deployment logs.
- Don't push fact refresh requests to the agent for undeployable resources. ([#7777](https://github.com/inmanta/inmanta-core/issues/7777))
- The retention policy of items in the agent cache can be set via the `evict_after_creation` and `evict_after_last_access` parameters.

- Update module documentation landing page

### Upgrade notes

- Agent cache retention policy parameter `timeout` is now an alias for the `evict_after_creation` parameter.

- Trace log level is no longer formatted as level 3 but as TRACE

### Deprecation notes

- Removed the 'inmanta module do' command ([#7913](https://github.com/inmanta/inmanta-core/issues/7913))
- Agent cache retention policy parameters `for_version` and `timeout` are deprecated. The `evict_after_creation` and `evict_after_last_access` parameters should be used instead.


### Bug fixes

- Compiler: fixed a rare occurrence of nondeterministic execution order ([#5145](https://github.com/inmanta/inmanta-core/issues/5145))
- Prevent the deletion of a project if this project contains one or multiple environments attached to it. ([inmanta/inmanta-core#7556](https://github.com/inmanta/inmanta-core/issues/7556))
- Fixed race condition where newly started agent may take 22 seconds to respond ([#7831](https://github.com/inmanta/inmanta-core/issues/7831))
- Don't export a new version if the compile fails, even if there are Unknown parameters

## Inmanta-ui: release 5.1.4 (2024-10-10)

No changelog entries.

## Web-console: release 2.0.0 (2024-10-10)

### Improvements

- Deploying Instance in the Composer saves the coordinates of the instance as metadata ([#5273](https://github.com/inmanta/web-console/issues/5273))
- From now on changing sorting on paginated Views resets pagination ([#5684](https://github.com/inmanta/web-console/issues/5684))
- First part of the Service inventory rework. Add skeleton structure for the Instance Details page. ([#5778](https://github.com/inmanta/web-console/issues/5778))
- Add the documentation tab to the Instance Details page. ([#5779](https://github.com/inmanta/web-console/issues/5779))
- Add the Attributes tab to the Instance Details page. ([#5780](https://github.com/inmanta/web-console/issues/5780))
- Improve the labels of Inter-Service Relation input fields ([#5922](https://github.com/inmanta/web-console/issues/5922))

### Bug fixes

- Resolve bug when JSON-editor is invalid on initial render. ([#5892](https://github.com/inmanta/web-console/issues/5892))

### Other notes

- Resolve security alert on micromatch by updating dependency
- Resolve security alert on webpack and path-to-regexp by updating dependency


# Release 2024.3.1 (2024-07-22)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 13.0.1 (2024-07-22)

### Upgrade notes

- If you had previously constrained `setuptools<71` in your project's `requirements.txt`, you may now drop the constraint

### Bug fixes

- Addressed breaking change in setuptools (core Python library)

## inmanta-ui: release 5.1.3
This component has had no new releases since the last product version.
## web-console: release 1.16.3
This component has had no new releases since the last product version.


# Release 2024.3 (2024-07-05)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 13.0.0 (2024-07-05)

### New features

- Compiler: Allow indexes on nullable attributes ([#7204](https://github.com/inmanta/inmanta-core/issues/7204))
- Add support to configure the logging framework using a configuration file. ([inmanta/inmanta-core#7271](https://github.com/inmanta/inmanta-core/issues/7271))
- Added support for forking agent executor ([#7524](https://github.com/inmanta/inmanta-core/issues/7524))

### Improvements

- Add support to the `GET /api/v2/discovered` endpoint to filter the discovered resources on whether they are managed or not.
 ([#6779](https://github.com/inmanta/inmanta-core/issues/6779))
- Remove the venv of an auto-started agent when its environment is deleted or cleared or when its project is deleted. ([inmanta/inmanta-core#7043](https://github.com/inmanta/inmanta-core/issues/7043))
- Raise a warning if JIT is enabled on the PostgreSQL database as this might result in poor query performance.
- Module release tool: do not write internal field `version_tag` to `setup.cfg`.
- Improve support for four-digit version on 'inmanta module release' command. If the 'use_four_digit' is set to 'True' in the module's metadata, the version will be bumped to a 4 digit format after a release. ([#7521](https://github.com/inmanta/inmanta-core/issues/7521))
- Remove references to `std::*` resources from the documentation ([#7563](https://github.com/inmanta/inmanta-core/issues/7563))
- Fix compiler handling of list constructors in plugin calls ([#7792](https://github.com/inmanta/inmanta-core/issues/7792))
- Display a banner in the docs that notifies the user when the build belongs to an old major iso version. ([inmanta/infra-tickets#201](https://github.com/inmanta/infra-tickets/issues/201))
- The server now also cleans up zombie processes, which is convenient when running in a container
- Update auth to be able to authenticate against a provided JWT
- Extend dict_path library, allow to resolve the wild cards of a wild dict path for a specific container.

### Upgrade notes

- The ``export`` command will now look for resource sets marked for deletion in the ``INMANTA_REMOVED_RESOURCE_SET_ID`` environment variable (As a space-separated list of sets to remove) in addition to the ones passed via the ``--delete-resource-set`` parameter.
 ([inmanta/lsm#736](https://github.com/inmanta/lsm/issues/736))
- The default retention time of the internal metrics store ('environment_metrics_retention') is reduced from one year to two weeks ([#7676](https://github.com/inmanta/inmanta-core/issues/7676))
- Handlers can now access the agent via 'inmanta.agent.executor.AgentInstance' instead of `inmanta.agent.agent.AgentInstance`. If you have developed a handler using `self._agent` to access agent internals, it may break.

### Bug fixes

- Fix race condition where exporting a file might fail if a file with the same content was uploaded between the file existence check in the database and the export itself.
 ([#7531](https://github.com/inmanta/inmanta-core/issues/7531))
- Fix bug that makes the endpoints to clear or delete an environment fail with the error message `(39, 'Directory not empty')`

## Inmanta-ui: release 5.1.3 (2024-07-05)

No changelog entries.

## Web-console: release 1.16.3 (2024-07-05)

No changelog entries.


## Web-console: release 1.16.2 (2024-07-05)

### New features

- Editing, Creating instances can now be done using a JSON editor. ([#5763](https://github.com/inmanta/web-console/issues/5763))

### Improvements

- Add functionality to filter instances through labels in the summary Pie Chart in Service Inventory ([#5710](https://github.com/inmanta/web-console/issues/5710))
- Improve the placement of the tooltip in the Resource Discovery page. ([#5730](https://github.com/inmanta/web-console/issues/5730))
- Update charts library to v7.3.0 to fix deprecation warnings ([#5756](https://github.com/inmanta/web-console/issues/5756))
- Refactor Authentication to simplify the flow and make it more maintainable and adjustable for new authentication providers ([#5759](https://github.com/inmanta/web-console/issues/5759))
- Allow the user to copy either the UUID or the identifier of an instance. ([#5764](https://github.com/inmanta/web-console/issues/5764))
- Add column for managed resources in the Resource Discovery page. ([#5765](https://github.com/inmanta/web-console/issues/5765))
- Add JWT authentication method to the application ([#5818](https://github.com/inmanta/web-console/issues/5818))
- Align the casing of the table headings in the discovered resource page.

### Bug fixes

- Update the filtering in the form to get Inter-service-relations. ([#5766](https://github.com/inmanta/web-console/issues/5766))
- Update the form to support editing deep nested embedded entities which have RW attributes in their attributes. ([#5792](https://github.com/inmanta/web-console/issues/5792))
- Update copy id/service_identifier icon to not be grayed out. ([#5827](https://github.com/inmanta/web-console/issues/5827))
- Fix the uri to managed resources on the discovery page. ([#5846](https://github.com/inmanta/web-console/issues/5846))


# Release 2024.2.1 (2024-05-24)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 12.1.0 (2024-05-24)

### Bug fixes

- Fixed a race condition where autostarted agents might become unresponsive for 30s when restarted ([#7612](https://github.com/inmanta/inmanta-core/issues/7612))
- Fix bug where the `GET /api/v2/resource/<rid>` and `GET /api/v2/resource` endpoints return an incorrect resourcestate if a resource moved back to the available state in a new version of the configurationmodel.
- Fix resource details endpoint status reporting

## inmanta-ui: release 5.1.1
This component has had no new releases since the last product version.
## Web-console: release 1.16.1 (2024-05-24)

### New features

- Add functionality to show relation label when hovering over them in Instance Composer ([#5623](https://github.com/inmanta/web-console/issues/5623))

### Improvements

- Automate axe compliance testing. ([#5154](https://github.com/inmanta/web-console/issues/5154))
- Added functionality to view instances that are blocked from editing in the Instance Composer. ([#5373](https://github.com/inmanta/web-console/issues/5373))
- Enable expert mode on empty values. ([#5588](https://github.com/inmanta/web-console/issues/5588))
- Forced state options are now sorted alphabetically. ([#5631](https://github.com/inmanta/web-console/issues/5631))
- Improve the icons in the menu to make them more straightforward. ([#5650](https://github.com/inmanta/web-console/issues/5650))
- Replace SVG icons with PatternFly icons. ([#5651](https://github.com/inmanta/web-console/issues/5651))
- Change information in the Composer's Form Modal to be more adequate when no instance is chosen, Make expand/collapse button action area bigger in the Instances on the Instance Composer Canvas. ([#5691](https://github.com/inmanta/web-console/issues/5691))
- replace randomUUID function with adequate cryptographic substitute ([#5706](https://github.com/inmanta/web-console/issues/5706))
- Propagate suggestions to embedded entities and allow 0 as valid default input ([#5717](https://github.com/inmanta/web-console/issues/5717))

### Bug fixes

-  resolve bug in duplicate form for preselected values in dropdowns. ([#5588](https://github.com/inmanta/web-console/issues/5588))
- Resolve a bug of invalid presentation of the add instance button in the instance composer when using Firefox ([#5689](https://github.com/inmanta/web-console/issues/5689))
- Resolve bug in resource details filtering, where removing log filters would send invalid request. ([#5697](https://github.com/inmanta/web-console/issues/5697))
- Fix issue with integers passed through expert mode as a string ([#5718](https://github.com/inmanta/web-console/issues/5718))
- Fix issue with updating textarea fields ([#5748](https://github.com/inmanta/web-console/issues/5748))


# Release 2024.2 (2024-04-02)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 12.0.0 (2024-04-02)

### New features

- Added support for arithmetic operators to the language (addition, substraction, multiplication, division, exponentiation and modulo). ([inmanta/inmanta-core#1799](https://github.com/inmanta/inmanta-core/issues/1799))
- Add facts that don't expire. ([#6560](https://github.com/inmanta/inmanta-core/issues/6560))
- Introduced a new configuration option `database.wait_time` for the Inmanta server, enabling it to wait for the database to become available before starting. Users can specify the maximum time (in seconds) the server should wait for the database to be up. A value of 0 means the server will not wait, while a negative value indicates the server will wait indefinitely. ([#6994](https://github.com/inmanta/inmanta-core/issues/6994))
- Implement constraints on jwt claims
- Remove state back propagation from the database

### Improvements

- Add `--soft-delete` option to the exporter. This option makes sure that resource sets, specified using the `--delete-resource-set` option, are only deleted if there are no resources exported for this set.
 ([inmanta/inmanta-lsm#1638](https://github.com/inmanta/inmanta-lsm/issues/1638))
- Report which pip indexes were used to install a V2 module or third-party Python dependency if that package could not be found. ([#6096](https://github.com/inmanta/inmanta-core/issues/6096))
- Add exclude_changes argument to the get_resource_actions endpoint to filter out resource actions with specific changes ([#6733](https://github.com/inmanta/inmanta-core/issues/6733))
- Improved error message when http request have oversized headers
- Improve performance of cross agent dependency resolution ([#6999](https://github.com/inmanta/inmanta-core/issues/6999))
- Improve exporter performance ([#7040](https://github.com/inmanta/inmanta-core/issues/7040))
- Improve performance of std::validate_type ([#7041](https://github.com/inmanta/inmanta-core/issues/7041))
- Add dedicated set_fact and set_parameter endpoints ([#7068](https://github.com/inmanta/inmanta-core/issues/7068))
- Remove support for legacy schema migration (< ISO4 ) ([#7117](https://github.com/inmanta/inmanta-core/issues/7117))
- Added the ability to have mergeable environment variables to the compiler service ([#7154](https://github.com/inmanta/inmanta-core/issues/7154))
- Improve performance of resource view ([#7231](https://github.com/inmanta/inmanta-core/issues/7231))
- Increased the default value of the database.connection_pool_max_size setting to 70 ([#7248](https://github.com/inmanta/inmanta-core/issues/7248))
- Improve deploy performance for very large models ([#7262](https://github.com/inmanta/inmanta-core/issues/7262))
- Add documentation on how to create the initial user when using the built-in authentication provider. ([inmanta/inmanta-core#7357](https://github.com/inmanta/inmanta-core/issues/7357))
- Ensure agent code folder is cleaned up on restart ([#7388](https://github.com/inmanta/inmanta-core/issues/7388))
- Agent started using std::Agentconfig now always deploy when first started ([#7448](https://github.com/inmanta/inmanta-core/issues/7448))
- Added a named-volume to the PostgreSQL server started by the docker-compose based installation documentation.
- Make agent more resilient to resource loading issues
- Improve performance by tuning logging
- Improve performance of type validation
- Make parameter refresh a non-blocking call
- Add support for string concatenation in the Inmanta modelling language
- Changed the default value of the `server.auth_method` config option from `None` to `oidc`.

### Upgrade notes

- The default value of the project configuration option `agent_install_dependency_modules` changed to True. ([inmanta/inmanta-core#7026](https://github.com/inmanta/inmanta-core/issues/7026))
- Remove state back propagation from the database

### Deprecation notes

- Remove functionality relying on netifaces from reporting. ([inmanta/inmanta-core#7019](https://github.com/inmanta/inmanta-core/issues/7019))
- The project configuration option `agent_install_dependency_modules` is deprecated and will be removed in a next major release. ([inmanta/inmanta-core#7026](https://github.com/inmanta/inmanta-core/issues/7026))

### Bug fixes

- Fixed bug where certain config options could not be set through environment variables
- Fix formatting of error message for inline if expressions ([#6226](https://github.com/inmanta/inmanta-core/issues/6226))
- make sure an environment can not be resumed while deleting, that deleting an environment first halts the environment and that the active model cannot be deleted.
- Resolve race condition on release version ([#6955](https://github.com/inmanta/inmanta-core/issues/6955))
- Deploy command no longer ignores ``-f`` option. ([#6993](https://github.com/inmanta/inmanta-core/issues/6993))
- Prevent deadlock between the `_log_session_expiry_to_db` and the `_log_session_seen_to_db` and `_log_session_creation_to_db` methods. ([inmanta/inmanta-core#7024](https://github.com/inmanta/inmanta-core/issues/7024))
- Requesting a dryrun after a partial compile was sometimes causing an internal server error. ([#7065](https://github.com/inmanta/inmanta-core/issues/7065))
- Fix bug where the latest released version of the configurationmodel could be removed by the cleanup job. ([inmanta/inmanta-core#7324](https://github.com/inmanta/inmanta-core/issues/7324))
- Improved f-string error reporting ([#7418](https://github.com/inmanta/inmanta-core/issues/7418))
- Fix bug where undefined and skipped_for_undefined resources are not correctly merged by the put_partial endpoint. ([inmanta/inmanta-core#7416](https://github.com/inmanta/inmanta-core/issues/7416))
- Fix a bug where PIP_NO_INDEX could be used by pip when use_system_config was set to False in the PipConfig ([#6096](https://github.com/inmanta/inmanta-core/issues/6096))
- Fix bug that causes literal values to be rendered incorrectly in the OpenAPI documentation. ([inmanta/inmanta-lsm#1586](https://github.com/inmanta/inmanta-lsm/issues/1586))
- Improve ha db setup documentation

## Inmanta-ui: release 5.1.1 (2024-03-29)

No changelog entries.

## Web-console: release 1.16.0 (2024-03-29)

### New features

- Add User Management view when user is logged in through database authentication ([#4738](https://github.com/inmanta/web-console/issues/4738))
- Discovered Resources page has been added. ([#5395](https://github.com/inmanta/web-console/issues/5395))
- New pages have been added to display the orders and their details. ([#5438](https://github.com/inmanta/web-console/issues/5438))
- Smart Composer is now general available ([#5470](https://github.com/inmanta/web-console/issues/5470))
- Add database based login form ([#5558](https://github.com/inmanta/web-console/issues/5558))

### Improvements

- Add filtering by resource type on the Compliance and Compare pages. ([#4555](https://github.com/inmanta/web-console/issues/4555))
- Prevent the user from creating a project name that could be an empty value. ([#5373](https://github.com/inmanta/web-console/issues/5373))
- Corrected the disabled highlight for disabled delete button in the Service Inventory ([#5400](https://github.com/inmanta/web-console/issues/5400))
- Improve Instance Composer code readability and remove duplicated code ([#5443](https://github.com/inmanta/web-console/issues/5443))
- Add description to the order api request and extract the call from the Canvas component ([#5469](https://github.com/inmanta/web-console/issues/5469))
- Add Tooltips to the icon buttons in the Instance composer ([#5478](https://github.com/inmanta/web-console/issues/5478))
- Add default behavior to zoom to fit on initial load of the instance in the Smart Composer ([#5506](https://github.com/inmanta/web-console/issues/5506))
- Adjusted the color of the compile details to match patternfly scheme. Added default empty page for facts. ([#5511](https://github.com/inmanta/web-console/issues/5511))
- Add support for suggestions in the forms ([#5531](https://github.com/inmanta/web-console/issues/5531))
- Added support to display attribute annotations in tabs in the Service Inventory ([#5532](https://github.com/inmanta/web-console/issues/5532))
- Update the add instance button to be displayed as a toggle when the Composer feature is enabled. ([#5554](https://github.com/inmanta/web-console/issues/5554))
- Update Notification Drawer to handle notifications without uri ([#5593](https://github.com/inmanta/web-console/issues/5593))
- Feature Flag V2, enable specific parts of the application based on licencing ([#5619](https://github.com/inmanta/web-console/issues/5619))
- Add improvements to smart composer: Highlight of loose components, Hide/Show connection label, composer is available only from root services
- Upgrade Yarn to V4.

### Bug fixes

- Enable adding new nested entity that are already part of a nested entity when the form is in edit-mode ([#5375](https://github.com/inmanta/web-console/issues/5375))
- Prevent displaying invalid dates in the Order Details View. ([#5512](https://github.com/inmanta/web-console/issues/5512))
- Fix display name in the form for inter-service relationship, and adjust filtering when clicking on a relation link in the attribute table. ([#5561](https://github.com/inmanta/web-console/issues/5561))
- Fix issue with misleading visual state of Diagnose button and misplaced 'back' button for terminated instances

### Other notes

- The repo requires node 18+ to be installed


# Release 2024.1.2 (2024-02-09)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 11.0.2 (2024-02-09)

### New features

- Prevent double processing of events in case of stale events ([#7066](https://github.com/inmanta/inmanta-core/issues/7066))

### Known Issues

- Handlers that process events should always indicate when they processed events(via ctx.set_updated) ([#7066](https://github.com/inmanta/inmanta-core/issues/7066))

## inmanta-ui: release 5.1.0
This component has had no new releases since the last product version.
## Web-console: release 1.15.3 (2024-02-09)

### Improvements

- Collapse Difference Viewer Component by default to improve loading performance - iso6 ([#5439](https://github.com/inmanta/web-console/issues/5439))


# Release 2024.1.1 (2024-01-22)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 11.0.1 (2024-01-04)

### Bug fixes

- Fix anchormap entrypoint (language server) for imports with rename

## inmanta-ui: release 5.1.0
This component has had no new releases since the last product version.
## Web-console: release 1.15.2 (2024-01-17)

### Bug fixes

- Fix resolving freezing of compliance check page


## Web-console: release 1.15.1 (2024-01-04)

### Bug fixes

- Fix for pagination in Service Inventory + tests


# Release 2024.1 (2023-12-11)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 11.0.0 (2023-12-11)

### New features

- Add 'exclude_change' argument to 'get_resource_events' to be able to exclude some types of changes from the results. ([#6375](https://github.com/inmanta/inmanta-core/issues/6375))
- Add server config option server.tz_aware_timestamps to make the server return time-zone aware timestamps. ([#6428](https://github.com/inmanta/inmanta-core/issues/6428))
- Add server config option server.tz_aware_timestamps to make the server return time-zone aware timestamps. ([#6428](https://github.com/inmanta/inmanta-core/issues/6428))
- A project-wide pip configuration can be set through the project.yml pip section. ([#6518](https://github.com/inmanta/inmanta-core/issues/6518))
- Introduce the 'float' type for floating point numbers ([inmanta/inmanta-core#6526](https://github.com/inmanta/inmanta-core/issues/6526))
- Introduced the dict_path module in the inmanta.util package. This module was previously located in the inmanta-lsm package. Users transitioning from inmanta-lsm should now use inmanta.util.dict_path for relevant functionality. ([inmanta/inmanta-core#6631](https://github.com/inmanta/inmanta-core/issues/6631))
- Support `*args` and `**kwargs` arguments in plugin signatures. ([inmanta/inmanta-core#6691](https://github.com/inmanta/inmanta-core/issues/6691))
- Migrated to pydantic v2, which offers more accurate type validation and increased performance

### Improvements

- Fixed reference to OpenAPI docs to work from any page
- Show exporter timings in compiler output ([#6387](https://github.com/inmanta/inmanta-core/issues/6387))
- Improve the output of the `inmanta compile` and `inmanta export` commands, by using the logger name `compiler`, `exporter` or `<name-inmanta-module>` for log records produced by respectively the compiler, the exporter or an Inmanta module. ([inmanta/inmanta-core#6489](https://github.com/inmanta/inmanta-core/issues/6489))
- Input validation of the put_version api endpoint is now more strict ([#6517](https://github.com/inmanta/inmanta-core/issues/6517))
- Rate limit resolution of cross agent dependencies and make notification asynchronous
- Stricter type checking of values returned by plugins.
- Set the ``PIP_PRE``, ``PIP_INDEX_URL`` and ``PIP_EXTRA_INDEX_URL`` pip env vars according to the project.yml pip config when activating an inmanta environment with the ``inmanta-workon`` command.
 ([#6721](https://github.com/inmanta/inmanta-core/issues/6721))
- Raise an explicit error when attempting to create a virtual env with invalid characters in its path.
- Added documentation on how to perform an upgrade in-place. ([inmanta/inmanta-service-orchestrator#393](https://github.com/inmanta/inmanta-service-orchestrator/issues/393))

### Upgrade notes

- All projects now require a pip config in the `project.yml`: please refer to the [migration guide](migrate_to_project_wide_pip_config) to move to a project-wide pip configuration. ([#6518](https://github.com/inmanta/inmanta-core/issues/6518))
- Stricter type checking of values returned by plugins. Specifying None as returned type requires None to be returned.
- For successful upgrading to this version, it is required to have ISO version 5.4.2 or higher already installed. ([#6726](https://github.com/inmanta/inmanta-core/issues/6726))
- stricturl is no longer supported. This has been dropped by pydantic

### Deprecation notes

- The ``net`` module has been deprecated. ([inmanta/net#209](https://github.com/inmanta/net/issues/209))
- The ``ip`` module has been deprecated. All its functionality is now available in the ``std`` module. ([inmanta/ip#253](https://github.com/inmanta/ip/issues/253))
- Remove the autostart_agent_interval and autostart_splay environment settings ([#6084](https://github.com/inmanta/inmanta-core/issues/6084))
- Deprecate the 'number' type. Use the 'int' or 'float' type instead ([inmanta/inmanta-core#6526](https://github.com/inmanta/inmanta-core/issues/6526))
- Removed the 'inmanta module install' command.. As an alternative to the now-removed 'inmanta module install' command, users should follow the updated procedure for module installation: The new method involves using the 'inmanta module build' command followed by 'pip install ./dist/<dist-package>' to build a module from source and install the distribution package, respectively. Alternatively, use 'pip install -e .' to install the module in editable mode ([#6717](https://github.com/inmanta/inmanta-core/issues/6717))

### Bug fixes

- Make sure openapi UI works when ssl is enabled ([#5680](https://github.com/inmanta/inmanta-core/issues/5680))
- Fix bug in f-strings not working when whitespaces surround the variable. ([#6629](https://github.com/inmanta/inmanta-core/issues/6629))
- Fix the handling of numeric keys in dict paths: floating-point numbers and their integer equivalents are treated as the same key. ([#6731](https://github.com/inmanta/inmanta-core/issues/6731))
- Fix a bug where numbers where cast to int instead of float
- Fix jwt config error message to use the correct attribute and provide more context
- Compiler: fixed bugs in some operators when "Unknown" values are passed: `==`, `!=`, `not`, `in` and `is defined` now properly propagate unknowns. ([#6033](https://github.com/inmanta/inmanta-core/issues/6033))
- Compiler: add support for "Unknown" values in operators ([#6033](https://github.com/inmanta/inmanta-core/issues/6033))
- No longer update the increment when the agent pulls (this is now done when a new version is released), to prevent race with #6486.
- Fixed compiler bug where list comprehensions result in a ListModifiedAfterFreeze exception when the value expression is a constructor

### Other notes

- Compiler: for consistency reasons, the for loop body will no longer be executed for "Unknown" values

## Inmanta-ui: release 5.1.0 (2023-12-11)

### Deprecation notes

- Removed the `web-ui.console_json_parser` option because it has become redundant. ([inmanta/inmanta-core#6641](https://github.com/inmanta/inmanta-core/issues/6641))

## Web-console: release 1.15.0 (2023-12-11)

### New features

- The Service inventory now supports the functionality to duplicate an instance. ([#5166](https://github.com/inmanta/web-console/issues/5166))

### Improvements

- Add links to API documentation, both for LSM API and the General API. The update Service Catalog message is now also clearer ([#4419](https://github.com/inmanta/web-console/issues/4419))
- Improve behaviour of the agents table when the environment is halted ([#4555](https://github.com/inmanta/web-console/issues/4555))
- Enhancement bringing back functionality to close Sidebar when clicked outside of it on mobile, Introduce said functionality to Notification Drawer - Desktop & mobile ([#4751](https://github.com/inmanta/web-console/issues/4751))
- Redirect the user to the Desired State page on Environment Creation on OSS, instead of Compile Reports page. ([#4835](https://github.com/inmanta/web-console/issues/4835))
- Highlight table rows when hovering ([#5038](https://github.com/inmanta/web-console/issues/5038))
- Add the attribute modifiers to the Service Details table. ([#5053](https://github.com/inmanta/web-console/issues/5053))
- Timestamps in the dashboard are now rounded to full hours ([#5081](https://github.com/inmanta/web-console/issues/5081))
- Introduce functionality that blocks UI for the process of halting environment ([#5136](https://github.com/inmanta/web-console/issues/5136))
- Increase default page size to 100 for Resource logs in the Resource details page. ([#5159](https://github.com/inmanta/web-console/issues/5159))
- The user actions present in the expanded rows in the Service Inventory, displaying the Service Details have been moved to a toggle-menu at the end of each row. ([#5166](https://github.com/inmanta/web-console/issues/5166))
- Update support archive link for v2 ([#5218](https://github.com/inmanta/web-console/issues/5218))
- Improve overal UI of the inventory table, and remove the Attribute Summary Column ([#5280](https://github.com/inmanta/web-console/issues/5280))

### Bug fixes

- Repair the drilldown height issue for the Actions dropdown. ([#5280](https://github.com/inmanta/web-console/issues/5280))


# Release 2023.4 (2023-10-13)

## General changes

### Upgrade notes

- The RPMs now install a Python 3.11 environment. ([inmanta/inmanta-core#6024](https://github.com/inmanta/inmanta-core/issues/6024))
- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 10.0.0 (2023-10-13)

### New features

- Add handler (DiscoveryHandler) to discover unmanaged resources. ([#6025](https://github.com/inmanta/inmanta-core/issues/6025))
- the `release_version`, `/version/<id>` api endpoint will now return a 409 when called twice on the same version ([#6349](https://github.com/inmanta/inmanta-core/issues/6349))
- Allow cron expressions in the agent_repair_interval so that we can specify a time-interval where the repair runs happen.

### Improvements

- Improve agents responsiveness for agents with a large number of connections and introduce a parameter to set the max-clients limit on an agent. ([#241](https://github.com/inmanta/inmanta-core/issues/241))
- add a warning to the docs about the risk of using multiple python package indexes
- Add top-level handler abstract base class `HandlerAPI` and made resource handlers generic in their resource type. ([#6025](https://github.com/inmanta/inmanta-core/issues/6025))
- Add the "not in" operator. ([#6211](https://github.com/inmanta/inmanta-core/issues/6211))
- Split deletes of projects, environments and configurationmodels into small transactions to prevent deadlocks. ([inmanta/inmanta-core#6427](https://github.com/inmanta/inmanta-core/issues/6427))
- Files handled by the file API are now stored in the database instead of on the file system of the Inmanta server. ([inmanta/inmanta-core#6441](https://github.com/inmanta/inmanta-core/issues/6441))
- Ensure that resources that will receive events are in the increment.. Any deployment with a status other than nochange is considered to be an event.  ([#6477](https://github.com/inmanta/inmanta-core/issues/6477))
- Add support for cron expressions for autostart_agent_deploy_interval and autostart_agent_repair_interval environment settings. ([#6549](https://github.com/inmanta/inmanta-core/issues/6549))
- Ensure child processes are awaited by the deploy command
- Prefix the error messages produced by the `inmanta module release` command with `Error:` to make clear it's an error message.
- Improve the output of the `inmanta compile` and `inmanta export` commands to make it more clear to the end-user when the command failed. ([inmanta/inmanta-core#5258](https://github.com/inmanta/inmanta-core/issues/5258))
- Increase the default value of INMANTA_MAX_ITERATIONS to 100000
- Moved the `validate_type` logic from the std module to inmanta-core. ([inmanta/inmanta-core#6540](https://github.com/inmanta/inmanta-core/issues/6540))
- Reduce log level of compiler scheduler from debug to trace, to reduce compiler log output
- Added support to the `GET /metrics` endpoint to round the returned timestamps to a full hour. ([inmanta/inmanta-core#6051](https://github.com/inmanta/inmanta-core/issues/6051))
- Add clarifying docstring to the IgnoreResourceException.

### Upgrade notes

- When implementing a generic handler (extending from Generic), the Generic class must be mentioned last in the list of base classes of that handler. ([#6025](https://github.com/inmanta/inmanta-core/issues/6025))
- the `release_version`, `/version/<id>` api endpoint will now return a 409 when called twice on the same version ([#6349](https://github.com/inmanta/inmanta-core/issues/6349))
- A full recompile is required after upgrading the Inmanta server to re-publish all required files to the file API. After the upgrade, the Inmanta server will no longer have access to files uploaded using the old version of the Inmanta server. ([inmanta/inmanta-core#6441](https://github.com/inmanta/inmanta-core/issues/6441))

### Deprecation notes

- The compiler no longer explicitly injects the implied `== true` for plugin calls in typedef constraints ([inmanta/inmanta-core#5787](https://github.com/inmanta/inmanta-core/issues/5787))
- The CRUDHandlerGeneric is now deprecated in favor of the CRUDHandler class ([#6025](https://github.com/inmanta/inmanta-core/issues/6025))
- The `server.delete-currupt-files` config option was removed. ([inmanta/inmanta-core#6441](https://github.com/inmanta/inmanta-core/issues/6441))
- Removed support for the legacy relationship syntax from the compiler. ([inmanta/inmanta-core#5265](https://github.com/inmanta/inmanta-core/issues/5265))

### Bug fixes

- Ensure get_resource_events and resource_did_dependency_change work across incremental compiles ([#5493](https://github.com/inmanta/inmanta-core/issues/5493))
- Prevent repairs from restarting indefinitely when a short deploy interval is set ([#6202](https://github.com/inmanta/inmanta-core/issues/6202))
- Ensure releasing a new version can not hide failures in ongoing deployments for older versions ([#6475](https://github.com/inmanta/inmanta-core/issues/6475))
- Increase the timeout on the status method of a server slice 1s to prevent undesired timeouts on the status page of the web-console. ([inmanta/inmanta-core#6599](https://github.com/inmanta/inmanta-core/issues/6599))
- Removed duplicate fact-expire from default config file
- Don't set a resource to the deploying state if that resource is undeployable.
- Fix bug where the `id.attribute_value` field of resources emitted by the exporter have a non-string type, when the type in the model is not a string.
- Improve the performance of the API endpoints that clear or delete an environment. ([inmanta/inmanta-core#6373](https://github.com/inmanta/inmanta-core/issues/6373))

## Inmanta-ui: release 5.0.0 (2023-10-13)

No changelog entries.

## Web-console: release 1.14.0 (2023-10-13)

### Improvements

- A banner will now be shown if your license is about to expire, or if it already has expired. ([#4708](https://github.com/inmanta/web-console/issues/4708))
- Add e2e test for keycloak authentication ([#4868](https://github.com/inmanta/web-console/issues/4868))
- Updated the default filtering on Compliance check page and Compare page to exclude the unmodified files. ([#4681](https://github.com/inmanta/web-console/issues/4681))
- Improve the error messaging when the server is down and not reachable. ([#4686](https://github.com/inmanta/web-console/issues/4686))
- Improve the user-feedback when pressing either the repair or deploy button on the ressource page. ([#4349](https://github.com/inmanta/web-console/issues/4349))
- Update url construction based on new changes in API to redirect to ressource page. ([#4907](https://github.com/inmanta/web-console/issues/4907))
- Refresh automatically the environment overview page. ([#4840](https://github.com/inmanta/web-console/issues/4840))
- The select for compare functionality on the Desired State page has been updated. ([#4391](https://github.com/inmanta/web-console/issues/4391))
- Implement the useFeatures hook to fetch the config.js file from the server and extract the features.

### Bug fixes

- Improve the behavior on Firefox when hovering over code-block icons. ([#4916](https://github.com/inmanta/web-console/issues/4916))
- Repair timepicker.

### Other notes

- Upgrade the UI library to Patternfly V5. ([#5076](https://github.com/inmanta/web-console/issues/5076))


# Release 2023.3 (2023-07-04)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 9.3.0 (2023-07-04)

### New features

- Added support for list comprehensions to the language, see the documentation for more details (Issue #5433)
- Added support for keyword-only arguments in plugins (Issue inmanta/inmanta-core#5706)
- Expose the logging setup through the stable api (Issue #5815)

### Improvements

- Add support to the compilerservice to request a compile that is part of a database transaction. (Issue inmanta/inmanta-lsm#1249)
- Add documentation on how to upgrade an orchestrator by migrating from one running orchestrator to another. (Issue inmanta/inmanta-service-orchestrator#391)
- The CRUDHandlerGeneric class was added. This class contains the same implementation as the CRUDHandler class, but is generic with respect to the specific PurgeableResource it acts on. (Issue inmanta/inmanta-core#5555)
- Added generic logging interface for the handler and a compatible implementation that uses the Python loggers for testing purposes. (Issue #5708)
- Add the "-v" / "--verbose" option to Inmanta commands and sub-commands to set the verbosity of the console output. (Issue inmanta/inmanta-core#5755)
- Add python-like f-strings. (Issue #5757)
- The 'inmanta module release' command now outputs the release tag (Issue #5816)
- Improve error reporting when attempting to move a resource to another resource set in a partial compile. (Issue #5884)
- Fix bug that makes the handler fail with the exception `PostgresSyntaxError: trailing junk after parameter at or near "$3A"` when running against PostgreSQL 15. (Issue inmanta/inmanta-core#5898)
- The server now keeps track of database pool exhaustion events and will report daily how many occured, if some exhaustion was noticed. (Issue #5944)
- improved support for pip config files by adding the use_config_file option to project.yml. If set the pip config file will be used. (Issue #5976)
- Add dedicated project-wide pip index url configuration option to the project.yml. (Issue #5993)
- Add support to expose the same method via the API using different URLs. (Issue inmanta/inmanta-lsm#1274)
- The hardcoded agent backoff time is now configurable using the `config.agent_get_resource_backoff` config option.
- Improve the documentation of the `api/v1/resource/<id>` endpoint and return a clear error message if the given id is not a valid resource version id.
- Improve the performance of the `GET /api/v2/resource/<resource_id>/logs` endpoint. (Issue inmanta/inmanta-core#6147)
- The server now logs the enabled extensions when it starts.
- Only print exception trace on cache failure when log level is at least DEBUG (-vvv)
- Ensure status endpoint returns after 100ms
- Update the documentation about setting up authentication, to use Keycloak version 20.0
- Mention in the server installation documentation which extensions need to be enabled.

### Upgrade notes

- The purge_on_delete feature and the `POST /decommission/<id>` endpoints have been removed. (Issue #5677)

### Deprecation notes

- In a future release it will not be possible anymore to use a resource with an id_attribute called id (Issue inmanta/pytest-inmanta#367)
- The CRUDHandler class is deprecated in favor of the CRUDHandlerGeneric class. In a future major release CRUDHandlerGeneric will be renamed to CRUDHandler. As such, it's recommended to import CRUDHandlerGeneric using the alias CRUDHandler. (Issue inmanta/inmanta-core#5555)
- Setting a package source in the project.yml file through the `repo -> url <index_url> option with type `package` is now deprecated in favour of the `pip -> index_urls <index_url> option.`
 (Issue #5993)
- For consistency, V1 modules' dependencies will now be installed using the configured pip index url (or v2 package repo) if it is set (Issue #5993)
- The default agent backoff time has been changed from five to three. This backoff is configurable using the `config.agent-get-resource-backoff` config option.
- Drop deprecated log_msg method in the handler.

### Bug fixes

- Show a clear error message when the `inmanta module freeze` command is executed on a v2 module. This is not supported. (Issue #5631)
- Don't run cleanup jobs on halted environments (Issue #5842)
- Make sure resource.version == resource.id.version (Issue #5931)
- The environment_delete endpoint now correctly removes the environment directory on the server. (Issue #5974)
- Fix bug in `inmanta module update` when requirements.txt contains additional constraints
- Fixed compiler bug that could lead to performance issues for deeply nested boolean operators
- Fix bug where the cleanup job, that removes old resource actions, ignores the environment scope of the `resource_action_logs_retention` setting. This way the shortest interval used for the `resource_action_logs_retention` environment setting across all environments was applied on all environments.
- Fixed broken link to Pydantic docs in documentation
- Fix issue where the documentation of the `inmanta module release` command is incorrectly formatted on the documentation pages.
- Make sure that the log line, that reports the time required for an agent to fetch its resources from the server, is reported as a floating point number instead of an integer.
- Fix race condition that can cause an environment setting to be reset to its default value.
- Fix bug that causes the `/serverstatus` endpoint to report an incorrect length of the compiler queue.
- The server no longer incorrectly logs a warning about server_rest_transport.token missing from the config

## Inmanta-ui: release 4.0.3 (2023-07-04)

### Improvements

- Improve the logging regarding the web-console configuration options.

## Web-console: release 1.13.0 (2023-07-04)

### Improvements

- From now on Recompile buttons aren't disabled after use, which makes queueing recompilations possible.
- Add support for Attribute-Type migration in the attribute table. (Issue #4534)
- Add support to run the e2e tests against the OSS Orchestrator releases. (Issue #4660)
- UI-fix for the header when authentication is enabled. (Issue #4865)
- Add support for textarea in forms (Issue #4910)

### Bug fixes

- Fixed issues with missing default values in string list input in Create Instance Form and with embedded entity inputs not being disabled in the Edit Instance Form (Issue #4737)
- Page redirection has been fixed when the authentication token expires. (Issue #4885)
- Bugfix for nested embedded entities being wrongly displayed in the attribute tree-table. (Issue #4915)


# Release 2023.2 (2023-04-11)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 8.3.0 (2023-04-11)

### New features

- Added namespace inference to nested constructors (Issue #4028)
- Add the user management service (Issue #5310)
- change agent_install_dependency_modules from experimental feature to expert feature (Issue #5693)
- adds docstrings to the anchormap so that the vscode extension can display them on hover (Issue inmanta/vscode-inmanta#933)

### Improvements

- Improve the performance of the `put_partial` endpoint (Issue inmanta/inmanta-core#4743)
- Expanded project's package repo documentation with a note about the risk of using multiple package repos and dependency confusion attacks.
- Old agents in the agent table are now cleaned up from the database. (Issue #5349)
- Improved compiler reasoning on resolving `is defined` for empty lists
- Improve line numbering when reporting non-existing attributes on constructors (Issue #5497)
- Produce no warning about download path if it is not used (Issue #5507)
- Added diagrams to the documentation that explain the limitations regarding inter-resource set dependencies when partial compiles are enabled. (Issue inmanta/inmanta-core#5679)
- Add support for four digit versioning for `inmanta module release`.
- Raise namespace lookup exception earlier (normalization phase) for improved diagnostics
- Added `-a` option to `inmanta release` command to commit all pending changes.

### Upgrade notes

- It's required to run a full compile on any environment that uses partial compiles after upgrading the server. (Issue inmanta/inmanta-core#4743)
- Changed the default value of `environment_agent_trigger_method` environment setting to `push_incremental_deploy`
- The `inmanta release` command will no longer do `git commit -a` by default, add the `-a` option to get the old behavior

### Bug fixes

- The following API endpoints now return their results in a consistent, meaningful order: methods.list_settings, methods_v2.environment_settings_list, methods.list_params, methods_v2.get_facts, methods.list_projects, methods_v2.project_list, methods.dryrun_list.
- Fix race condition that causes the deployment of a resource to fail with the error message: 'Fetching resource events only makes sense when the resource is currently deploying'. This issue happens in rare situations and the orchestrator will automatically recover from it during the next deployment.
- Fix issue that may cause the first export for an environment to fail when files with identical content are present.
- Autostarted agents will now log in debug mode (Issue #5562)
- Fix bug that incorrectly calculates the timestamp indicating which facts have to be renewed.
- Fix race condition in incremental deploy calculation where a newly released version uses an increment that is calculated from an old model version.
- Fix bug where the 'done' field of a model version returned by the `GET /version` or the `GET /version/<id>` API endpoint decrements when a repair run of an agent changes the state of the resource to deploying again.


## Inmanta-core: release 8.2.0 (2023-02-09)

### Improvements

- Support `inmanta module release` options `-c`, `--patch`, `--minor`, `--major` without `--dev`

## Inmanta-ui: release 4.0.2 (2023-04-11)

No changelog entries.

## Web-console: release 1.12.3 (2023-04-11)

### New features

- Add support to force instance state, destroy instance or change intance attributes through lsm expert mode (Issue #4682)

### Improvements

- Move sidebars status icon into Header (Issue #4342)
- Adding automated e2e testing for the Resources (Issue #4367)
- Improve appeareance of Environment selector and move it to the right corner of the page (Issue #4531)
- Add new icons for new event types in Service Inventory (Issue #4609)
- Improve support for attribute lists (Issue #4556)

### Bug fixes

- Resolve the rounding issue on dashboard Service Counter. (Issue #4602)
- refresh catalog list after deleting Service (Issue #4608)
- Show no value instead of null when there is no description in embedded/relation entity (Issue #4610)
- Fix tooltip aligment and resolve flickering on environment control button (Issue #4612)
- Allow to add/delete optional nested entities (Issue #4615)
- Fix service details relation links to send user to specified service page (Issue #4617)
- Fix incorrect Y-axis values on stacked charts on dashboard (Issue #4626)
- Improve metrics tooltip placement across chart (Issue #4627)
- Fix issue wit clearing unread notification (Issue #4677)
- fix the issue that crash the app when using missing environment setting and it's definition (Issue #4772)


# Release 2023.1.1 (2023-02-17)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## inmanta-ui: release 4.0.1
This component has had no new releases since the last product version.
## Web-console: release 1.12.2 (2023-02-17)

### Bug fixes

- Do not show LSM related graphs when LSM it not loaded (Issue #4650)


## Web-console: release 1.12.1 (2023-02-09)

No changelog entries.


# Release 2023.1 (2023-02-06)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 8.1.0 (2023-02-06)

### New features

- Added `inmanta module release` command. (Issue inmanta/inmanta-core#5082)
- Added the `/metrics` API endpoint to retrieve aggregated metrics about an Inmanta environment from the server. (Issue inmanta/inmanta-core#5129)
- experimental: Added a project option to install dependencies on other modules when loading code on the agent
- Improve stability of incremental deploy for resources containing dicts (Issue #5306)

### Improvements

- Remove resource.resource_version_id fields from the database and use resource id instead
- Improve error reporting when an index collision is detected. (Issue #5075)
- A proper inmanta warning is now displayed when an invalid escape sequence is detected in a regular string or a multi-line string. (Issue #5091)
- Fix wrong docker login instructions
- improved partial compile documentation for LSM
- Improved error reporting when an optional list attribute (not relation) remains unset
- Improved exception handling during shutdown
- Remove auto-recompile-wait from the config file in the rpm (Issue #4332)

### Upgrade notes

- The first recompile after this upgrade will always perform a full deploy (Issue #5306)

### Deprecation notes

- The `inmanta module commit` command has been deprecated in favor of the `inmanta module release` command.
- The `do_clean_hard` and `postgres_get_custom_types` functions and the `PGRestore` and `AsyncSingleton` classes in respectively `inmanta_tests.conftest` and `inmanta_tests.db.common` were moved to the `inmanta.db.util` module. The `do_clean_hard` function is available in the `inmanta.db.util` module under the name `clear_database`. These functions and classes will be removed from their original location in a future major release (>=ISO7). (Issue inmanta/inmanta-core#5383)

### Bug fixes

- Fix issue where server-side compiles fail when the SSL configuration on the server doesn't match the SSL configuration defined in the .inmanta file of the project. (Issue inmanta/inmanta-core#4640)
- Fixed cycle detection in experimental relation precedence policy (Issue #5380)
- Fix handling of deploying state in incremental deploys (Issue #5434)

## Inmanta-ui: release 4.0.1 (2023-02-06)

No changelog entries.

## Web-console: release 1.12.0 (2023-02-06)

### New features

- Create component and navigation for the Dashboard Page (Issue #4525)
- Create base components for Dashboard, endpoint QueryManager to acquire metrics and serve them to Dashboard and finally components with given Manager (Issue #4527)
- Adjust routing to include Dashboard correctly, fix e2e accordingly to new flow of routes (Issue #4531)
- Add interpolation to charts when no data was aggregated, format dates from UTC to local, add rounding (Issue #4579)

### Improvements

- Adding automated e2e testing for the Service Catalog, for a basic-service instance. (Issue #4317)
- Adding automated e2e testing for the Service Catalog, for child-parent service instances. (Issue #4320)
- Adding automated e2e testing for the Service Catalog, for a Embedded Entity instance. (Issue #4321)
- Adding automated e2e testing for the Service Catalog - Catalog Update (Issue #4323)
- Adding automated e2e testing for the Service Details (Issue #4327)
- Adding automated e2e testing for the Service Catalog, for a desired state (Issue #4337)
- Adding Tooltips for halted and resume buttons in the sidebar. (Issue #4341)
- Adding automated e2e testing for the Compile Reports (Issue #4348)

### Bug fixes

- Fix Service filtering when clicking on service relation (Issue #4099)
- Fix toolbar alignment issue. (Issue #4422)
- Fix form booleans issue (Issue #4438)
- Name of the agent is not properly escaped in pause agent request (Issue #4454)
- Fix resource logs issue (Issue #4480)
- Fix configuration update issue (Issue #4481)
- fixes to metrics (Issue #4590)


# Release 2022.4 (2022-12-01)

## General changes

### New features

- Add support for RHEL 9 and derivatives. (Issue inmanta/inmanta-core#4973)

### Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 8.0.0 (2022-11-30)

### New features

- Added the inmanta-workon command (Issue #4376)
- Add the finalizer decorator. Functions decorated with it will be executed at the end of the compilation
- Constructors that appear as a right hand side in an assignment (or another constructor) now no longer require explicit assignments for the inverse relation to the left hand side.
- Add support for extensions to register their environment settings via the `register_environment_settings` method in the `extension.py` file of the extension. (Issue inmanta/irt#1366)

### Improvements

- Improve the logging of the pip commands by using a separated logger for those. Also add the content of the requirements and constraints files to the logging. (Issue #4651)
- Add module and plugin deprecation mechanism (Issue #4908)
- Improve the error message when trying to build a moduleV2 with an invalid version name (Issue #5054)
- Refactor page view functionality

### Deprecation notes

- Remove support for leaving nullable attribute unassigned, an exception will now be raised. You should make sure optional variables are always assigned a value. This changes the behaviour of 'is defined' in Jinja templates. You should now use 'is not none' instead (Issue #1888)
- The 'dashboard' section is no longer supported for configuration options. The 'web-ui' section should now be used instead for configuration options related to web interfaces. (Issue inmanta/inmanta-ui#317)
- The Inmanta dashboard was removed. The URL of the Inmanta dashboard now redirects to the Inmanta web-console which is the successor of the Inmanta dashboard. (Issue #4905)
- V1 modules are deprecated. Support for V1 modules will be removed in one of the next major releases (Issue inmanta/inmanta-core#4941)
- Removed support to use a dictionary in the requires metadata field of a V1 module or an Inmanta project. (Issue inmanta/inmanta-core#4974)
- The `inmanta module update` command and the `-r` option of the `inmanta module list` command were removed. They are replaced by the `inmanta project update` and the `inmanta project freeze` command respectively. (Issue inmanta/inmanta-core#4975)
- Remove support for hyphens in identifiers. An exception will now be raised. (Issue #4976)
- The available-versions-to-keep option of the server configuration file is no longer supported. Please use the AVAILABLE_VERSIONS_TO_KEEP environment setting instead. (Issue #4980)
- Remove support for default constructors (Issue #4984)
- The `inmanta.server.services.environmentservice.register_setting` method, used by the extensions to register environment settings, has been deprecated. The `register_environment_settings` method in the `extension.py` of the extension has to be used instead. (Issue inmanta/irt#1366)

### Bug fixes

- Fix issue where the progress information of the git clone command shows mixed log lines (Issue inmanta/inmanta-core#4919)
- Fix issue with "inmanta module build" command on a v1 module if inmanta_plugins dir already exists (Issue #4954)
- Fix bug where the stdout filehandler is not closed after streaming the output from pip into the logger.
- Fix bug where warnings messages were not shown to the user.
- Fix bug where the status endpoint can become non-responsive
- Fix issue where the documentation of the `inmanta module freeze` command incorrectly indicates that it updates the project.yml file, while it updates the module.yml file.
- Fix an issue about the __str__ function of the DatabaseOrder class which made it incompatible with python3.11
- Fix an issue about enum representation which made a test fail for python3.11
- Fixes an issue about optional fields without default value not being populated correctly in DAO
- Fix bug where a ResourceAction fails with an InvalidStateError when the agent is shutdown
- Fix bug where the endpoints `compile_details`, `get_compile_reports` and `get_compile_queue` returned incorrect data for the fields `exporter_plugin`, `notify_failed_compile` and `failed_compile_message`.

## Inmanta-ui: release 4.0.0 (2022-11-30)

### Deprecation notes

- The 'web-console' section is no longer supported for configuration options. The 'web-ui' section should now be used instead for configuration options related to web interfaces. (Issue inmanta/inmanta-ui#317)

## Web-console: release 1.11.3 (2022-11-30)

### Improvements

- Allow to send filter values from more than one input at once with enter or button click - Resouces & Desired State Details view
- An update banner will be displayed if your application happens to be outdated. (Issue #3879)
- Add an indication in the navigation sidebar when there are ongoing compilations. The indication will be added to the "Compile Report" menu-item.
- add buttons for expanding/collapsing all nested attributes to speed up the process of going through services
- The create/edit Instance form now has a better way to allow the user to select multiple Inter Service Relations. (Issue #4100)
- Updating React version to React 18. (Issue #4107)
- The link to the old dashboard has been removed from the sidebar. (Issue #4108)
- Improve the sidebar closing behaviour when on smaller screens. You can now click in the page content to close the container. (Issue #4119)
- Add Hooks that check if user leaves unfinished Add/Edit Instance form and prompt for confirmation (Issue #4125)
- When only one option available in select input, then this one is preselected instead of default placeholder prompt (Issue #4127)
- A button has been added to the Service Catalog overview to execute an update. (Issue #4159)
- move service details from dropdown to separate page (Issue #4160)
- add pagination on the bottom of the table to improve UX (Issue #4246)
- Move delete service button to the Service Catalog overview, in the kebab menu options. (Issue #4326)
- Fix service callbacks issues in display, in readabilty and form behaviour after adding callback (Issue #4332)
- Fix filter options being displayed under the DIFF comparator on some pages. (Issue #4338)
- Improve alignment of filter options on smaller screens. (Issue #4339)

### Bug fixes

- Fix missing paramter in query when updating a service configuration. (Issue #4064)
- Fix the error thrown on create new instance. (Issue #4100)
- Make sure the Update button is also shown on an empty Catalog.
- Hotfix for the xml-formatter when the scenario occurs where the string to be formatted is preceded or ends with whitspaces. (Issue #4144)


# Release 2022.3 (2022-09-29)

## General changes

### Upgrade notes

- Ensure the database is backed up before executing an upgrade.

### Bug fixes

- Add a signal handler to the entrypoint of the Inmanta container to correctly handle the termination of the container

## Inmanta-core: release 7.1.0 (2022-09-29)

### New features

- Add option to bytecompile all python source in a v2 module wheel (Issue inmanta/irt#1190)
- Replace Drupal model of quickstart with SR Linux. (Issue #4333)
- Added partial compile feature

### Improvements

- When the AutostartedAgentManager starts a new agent process, it now uses a dynamic timeout on the time to wait until all agents are active. The AutostartedAgentManager raises a timeout as soon as no new agent has become active in the past five seconds. (Issue inmanta/inmanta-core#4398)
- Improved logging on the agent manager when restarting agents
- Performance improvements for the resource_did_dependency_change endpoint (Issue #4402)
- The `put_partial` endpoint and `inmanta export --partial` now dynamically allocate a new version.
- Add support for extras on Python dependencies (Issue inmanta/inmanta-core#4497)
- Improve logging on module installation. (Issue #4500)
- Reject v1tov2 module conversion when a setup.py is present
- Fix issue where the v1tov2 command removes the requirements.txt file (Issue #4684)
- Fix a bug in the typing of the new influxdb metrics (Issue #4688)
- Don't set PYTHONPATH environment variable on venv activation: fixes editable install compatibility with setuptools<64 (Issue #4713)
- Add argument to compilerservice to allow exporting with the specified exporter plugin
- Added options to compiler service to configure notification behavior (Issue #4803)
- Reduce compiler log level for iterations and cache log lines to debug
- For v1tov2 conversion, split tag from version and put it in tag_build field
- Improved editable v2 module compatibility with latest setuptools and PEP660 in edge case scenarios.
- Set the startup/shutdown order between the Inmanta server and the database in the docker-compose file

### Upgrade notes

- It's required to update-and-recompile on each Inmanta project on the server after an upgrade (Issue inmanta/inmanta-core#4718)

### Deprecation notes

- The internal upload_code endpoint has been removed, deprecated since core release 2018.2 (Issue inmanta/irt#1190)
- The `put_partial` endpoint (previously marked experimental) no longer accepts a version argument.

### Bug fixes

- Fix rare deadlock in the database locking mechanism when tasks are cancelled, mostly affects test environments. (Issue #4384)
- Fix issue that causes an agent restart storm for all agents on an agent process when an agent on that process is paused. (Issue inmanta/inmanta-core#4398)
- make sure that the index present in PIP_INDEX_URL or PIP_EXTRA_INDEX_URL is not leaked to pip when using install_from_index (Issue inmanta/inmanta-core#4723)
- Fix issue where the pip consistency check is too strict (Issue #4761)
- The compiler service now logs the requested time of a recompile using a consistent timezone
- Fixed minor backwards incompatibility of the resource action database schema and `resource_action_update` endpoint
- Fix bugs in the merge logic of a partial compile. 1) Ensure that the version numbers present in the new version of the configuration model are set correctly. 2) Ensure that the resource states and unknowns, that belongs to the partial model, are sent to the server and merged correctly with the old configuration model.

## Inmanta-ui: release 3.0.2 (2022-09-29)

No changelog entries.

## inmanta-dashboard: release 3.8.1
This component has had no new releases since the last product version.
## Web-console: release 1.11.2 (2022-09-29)

### Improvements

- add delete button for desired state version with test coverage, bump test coverage for sibiling components (Issue #3957)
- replace KeyCloakInstance as it is depraceted (Issue #4002)

### Upgrade notes

- Improve test coverage for conditionals (Issue #4000)

### Bug fixes

- Scroll into view when new lines are being added to the report while it is compiling. (Issue #3855)
- Fix the overflow disapearing outside the window for the facts table. (Issue #3909)
- Add error handling for uncaught errors. (Issue #3924)
- replace instance uuid with instance identity when possible in action modals(Delete and set State Action)
- bump dependencies versions to resolve vulnerabilities (Issue #4001)
- Fixed issue where web-console would crash when failing to format xml

### Other notes

- The editorconfig file now ensures that the codebase stays LF, the package.json will contain Windows specific commands for linting/prettier. Single quotes for paths are not supported by Windows. (Issue #3909)
- updated the jenkins scripts for tests to be slightly more performant (Issue #3924)


# Release 2022.2.1 (2022-08-16)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## inmanta-core: release 7.0.0
This component has had no new releases since the last product version.
## inmanta-ui: release 3.0.1
This component has had no new releases since the last product version.
## inmanta-dashboard: release 3.8.1
This component has had no new releases since the last product version.
## Web-console: release 1.11.1 (2022-08-16)

### Bug fixes

- Fixed error on settings page resulting in blank page
- Fixed behavior of instance creation and update for services with inter-service relations


# Release 2022.2 (2022-08-08)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 7.0.0 (2022-08-05)

### New features

- Change the relation deprecation warning to be more accurate. (Issue #2443)
- Add support for the elif keyword to the compiler
- Improved tracking of potential future relation assignments within conditional statements.
- Improved error reporting for invalid namespace access (Issue #2818)
- Expressions are now treated as statements (Issue #3367)
- Add environment setting to set the number of stored versions. (Issue #3505)
- Ensure processes forked by Inmanta commands load the same config folder as their parent process (Issue #3765)
- Add notification service (Issue #3981)
- Create a notification when a git pull fails during compile (Issue #4021)
- Add 'inmanta-cli environment recompile' command (Issue #4052)
- Added auto_full_compile environment option to schedule regular full compiles (Issue #4274)
- Add support to pass type precedence hints to the compiler (Issue #3098)
- Added support to create development builds of V2 modules (Issue inmanta/irt#1184)
- Added documentation for primitive type casts to the language reference

### Improvements

- Improve batching of code loading in the agent (Issue #4217)
- inmanta module v1tov2 and inmanta module build will now merge setup.cfg and pyproject.toml (Issue #4372)
- Add py.typed file to packages build using inmanta module build (Issue #4374)
- The compiler cache (.cfc) files are now stored in the .cfcache directory in the root of the inmanta project instead of in the __cfcache__ directory in the inmanta modules. (Issue inmanta/inmanta-core#4407)
- More precise cache invalidation for the compiler cache (Issue #4408)
- Add support to enable/disable strict dependency checking in the compiler and in the module tools using the --strict-deps-check and --no-strict-deps-check options. (Issue #4516)
- Improve exception messages on version conflicts (Issue #4524)
- Improve documentation of agent configuration
- Make `python -m inmanta` work
- Add database connection metrics to the influxdb reporter

### Upgrade notes

- The default log level of the `inmanta` commandline tool was changed from ERROR to WARNING (Issue #3911)
- The compiler and the module tools now by default check all dependencies transitively for version conflicts. When a version conflict is found, an error is raised. A fallback to the old behavior is possible by providing the `--no-strict-deps-check` option. (Issue #4516)
- `inmanta project install` and `inmanta project update` now always take into account the `requirements.txt` of the project to provide additional version constraints to pip (Issue #4410)

### Deprecation notes

- Unicode characters are no longer escaped in multi-line strings. (Issue #2582)
- The available-versions-to-keep option in the server configuration file is now deprecated in favor of the environment setting (Issue #3505)
- Writing a string over multiple lines is now only supported for strings within triple quotes. This was previously allowed for strings within single quotes due to a bug.
- An exception is now raised when trying to interpolate a string in a dictionary key
- The auto-recompile-wait option in the server configuration is now deprecated in favor of the recompile_backoff environment setting (Issue #4332)

### Bug fixes

- The logger now correctly reports the endpoints that will be removed from a session
- Fixed an instance of nondeterministic behavior in the compiler
- Fix memory leak caused by lru-cache keeping strong references to cached items
- Optimize resource list query
- Fix installing extras of module dependencies (Issue #3443)
- Fix bug that fails the CRUDHandler when a changed attribute is of type set. (Issue #3470)
- Wrap any exception that occurs during resource export so that it is more useful to the end user (Issue #3787)
- Writing a string over multiple lines is now only supported for strings within triple quotes.
- An error message is now shown if a wrong repo path is used
- An exception is now raised when there is a mismatch between the python version of the compiler venv and the python version of the active process (Issue #3829)
- Improve the compiler error message that is given when an index attribute is missing in the constructor call. (Issue #3902)
- Fix bug where the user is suggested to run the `inmanta module update` command when the execution of the same command failed. (Issue #3911)
- Fixed bug that makes the `inmanta deploy` command fail when the database and server sections of the inmanta configuration files contain non-default values. (Issue #3927)
- Fix bug that makes every inmanta warning end with an empty line. (Issue #3951)
- Improve syntax error reporting when defining an attribute starting with a capital letter.
- Fix handling of '_' in resource_logs and get_resource_events api endpoints (Issue #4043)
- Fix bug where `inmanta project install` and `inmanta project update` always invokes pip, even when all dependencies are already met. (Issue #4055)
- Limit included namespace packages to inmanta_plugins for v1tov2 module conversion. (Issue #4130)
- Enforce inmanta package requirements so that modules can't overwrite those. (Issue #4200)
- Make sure that the `inmanta project install` command doesn't protect the inmanta-dev-dependencies package (Issue #4249)
- Fix syntax error when calling "is defined" on dictionary lookup
- The set_setting endpoint now correctly returns a 400 status code when an invalid value is provided. (Issue #4361)
- Fix bug where the setup.cfg file, generated by the v1tov2 command, contains a dependency to the module itself when the module contains an import for a namespace in its own module. (Issue inmanta/inmanta-core#4373)
- Fix bug on value lookup in an unknown dict and on lookup with an unknown key. (Issue #4475)
- Fix failing test case.
- Fix order of stages in compile report details (Issue inmanta/web-console#3082)
- Fixed incorrect top level module loading for nested imports when v2 module is present in venv but not in explicit requires
- Fix performance impacting race condition in deploy handler method (Issue inmanta/lsm#433)
- Fix issue with get_resources_in_latest_version call not taking into account versions without resources (Issue inmanta/inmanta-lsm#739)
- Fix issue where the deployment of resources takes a long time, due a high rate limiter backoff. (Issue #4084)
- Fixed type cast behavior for `null` and unknown values

## Inmanta-ui: release 3.0.1 (2022-08-05)

No changelog entries.

## inmanta-dashboard: release 3.8.1
This component has had no new releases since the last product version.
## Web-console: release 1.11.0 (2022-08-05)

### New features

- Add support for inter-service relations in the service inventory (Issue #3040)


# Release 2022.1.1 (2022-04-19)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 6.0.2 (2022-04-19)

### Bug fixes

- Fix bug that crashes the agent when a cross-agent dependency doesn't have any changes (Issue #4116)
- Constrained click dependency to known compatible range because of backwards incompatible minor

## Inmanta-core: release 6.0.1 (2022-02-11)

### Bug fixes

- Fix bug in incremental deploy where event processing can be delayed (Issue #3789)

## inmanta-ui: release 3.0.0
This component has had no new releases since the last product version.
## inmanta-dashboard: release 3.8.1
This component has had no new releases since the last product version.
## Web-console: release 1.10.0 (2022-04-12)

### New features

- Add the Compliance Check page (Issue #2558)
- Add notification drawer (Issue #3056)
- Add notification center page (Issue #3067)

## Web-console: release 1.9.1 (2022-02-11)

### New features

- Add Desired State Compare page (Issue #2374)


# Release 2022.1 (2022-02-03)

## General changes

### New features

- Added the web console as the default front-end, replacing the dashboard (Issue #65)
- Introduced the [v2 module format](https://docs.inmanta.com/community/latest/model_developers/modules.html#understanding-modules). V2 modules offer better integration with the Python ecosystem with regards to [distribution](https://docs.inmanta.com/community/latest/model_developers/modules.html#installing-modules), dependency resolution and plugin loading. For more information on v2 modules, see how to [add a v2 module source](https://docs.inmanta.com/community/latest/model_developers/developer_getting_started.html#v2-module-source), [use a v2 module in your project](https://docs.inmanta.com/community/latest/model_developers/developer_getting_started.html#setting-up-a-module), and [install v2 modules](https://docs.inmanta.com/community/latest/model_developers/modules.html#installing-modules).
- Added support for Python 3.9
- Added deploy method to handlers for increased flexibility in responding to events (Issue inmanta/inmanta-core#2940)
- Added raw strings (r-strings) to the inmanta language (https://docs.inmanta.com/community/latest/language.html#literals-values)
- Added support for Jinja 3 to std module.
- Added terraform module. Allows to use native terraform providers without having to use terraform directly by using the included model generator. (https://docs.inmanta.com/community/latest/reference/modules/terraform.html)
- VSCode extension interacts with the Python extension to allow venv selection.
- Extended web console functionality and made it the default front-end.

### Upgrade notes

- Compiling a project no longer installs modules on the fly. Run `inmanta project install` to install modules. For more details see [setting up a project](https://docs.inmanta.com/community/latest/model_developers/developer_getting_started.html#setting-up-a-project).
- The compiler venv (`.env`) is no longer used. The compiler uses the active venv.
- The supported PostgreSQL version is now 13
- The supported Python version is now 3.9
- This release requires RHEL 8
- Jinja templates are required to be compatible with [Jinja 3](https://jinja.palletsprojects.com/en/3.0.x/changes/#version-3-0-0).
- An update of the VSCode extension is required for compatibility with this release.
- Clear your browser cache after upgrading to remove the old redirection rule. If the cache is not cleared the ‘/’ route will keep redirecting to ‘/dashboard’.
- The compiler and agent venv's with a Python version older than the Python version of the Inmanta server will be moved to an `.rpmsave` directory at installation time. (Issue inmanta/inmanta-service-orchestrator#234)
- Ensure the database is backed up before executing an upgrade.

### Deprecation notes

- `inmanta module install` no longer installs all modules for a project. This has moved to `inmanta project install`.
- The inmanta dashboard is now deprecated in favor of the web console. It will be removed in a future major release.

## Inmanta-core: release 6.0.0 (2022-02-02)

### New features

- Added `resource_deploy_start` endpoint (Issue #2928)
- Added `resource_deploy_done` endpoint (Issue #2931)
- Added helper method for reliable event processing (Issue #2941)
- Improved south bound integration documentation (Issue #2954)
- Compiler improvement: made `is defined` gradually executable
- Added `resource_list` endpoint (Issue #3045)
- Added `resource_details` endpoint (Issue #3046)
- Added support to build V2 modules into a Python package. (Issue #3047)
- Added `resource_history` endpoint (Issue #3048)
- Added the ability to package V1 modules as V2 modules (Issue #3049)
- Added `inmanta module v1tov2` command. (Issue #3050)
- Added V2 package loader (Issue #3051)
- Updated `inmanta module install` to install v2 modules from source.
- Added the `inmanta module add` command. (Issue #3089)
- Added `resource_logs` endpoint (Issue #3109)
- Added endpoint to list compile reports (Issue #3131)
- Added endpoint to get compile details (Issue #3132)
- `inmanta project update` now updates modules' Python dependencies to the latest compatible version. The same goes for triggering an update and recompile from the dashboard. (Issue #3623)
- Enable the UI extension by default (Issue #3653)
- Added version diff api endpoint (Issue #3659)
- Added raw strings to the inmanta language.
- Restructured module developer guide
- added operational procedures documentation
- added instructions about passwordless sudo to remote agent setup
- Added documentation regarding modules V2. (Issue #3023)
- Port the agent to the new `deploy` handler method. (Issue #2940)
- Added support for PostgreSQL 13 (Issue #2893)

### Upgrade notes

- On newly created environments, the environment setting `purge_on_delete` will be set to false by default instead of true. This overrides any purge_on_delete settings on individual resources. You need to explicitly set it to true to enable the old behavior again. (Issue #2958)
- `inmanta compile` no longer installs any modules. Run `inmanta project install` before compiling the first time.
- "The compiler venv has been phased out. The compiler will now use the venv used to execute the `inmanta compile` command."
 (Issue #3096)
- Compiler no longer installs modules on the fly, `inmanta project install` needs to be run to install required modules
- Clear your browser cache after upgrading to remove the old redirection rule. If the cache is not cleared the '/' route will keep redirecting to '/dashboard'.  (Issue #3497)
- `Project.load()` no longer installs Project dependencies. Pass `install=True` for the old behavior.
- NOTSET is no longer accepted as a log level by the agent's context logger.
It was not a valid log level before, but it was accepted by the agent.

- After upgrading the Inmanta server, all virtual environments used by the compiler and the agents have to be removed. Use the following procedure to achive this:
  * Stop the Inmanta server
  * Remove all `/var/lib/inmanta/server/environments/<environment-id>/.env` directories
  * Remove all `/var/lib/inmanta/<environment-id>` directories
  * Start the Inmanta server again


### Deprecation notes

- `inmanta module install` no longer installs all modules for a project. This has moved to `inmanta project install`.
- The `inmanta module list -r` command has been deprecated in favor of `inmanta project freeze`
- `inmanta modules update` has been replaced by `inmanta project update`. The old command has been deprecated and will be removed in a future release. (Issue #3623)

### Bug fixes

- Fixed docstring-parser compatibility after non-backwards compatible changes and constrained dependency to semi-safe range.
- Ensure that special characters in the resource action log are not escaped. (Issue inmanta/inmanta-lsm#699)
- Fixed agent cache behavior when `cache_none` is provided
- Fix dollar sign escaping issue in installation documentation
- Fix bug where the listeners of the environment clear action are not notified when files of that environment cannot be deleted from the filesystem. (Issue #3637)
- The tests folder is no longer included into the sdist package
- Removed NOTSET loglevel from all API's

## inmanta-ui: release 3.0.0
This component has had no new releases since the last product version.
## Inmanta-dashboard: release 3.8.1 (2022-01-25)

No changelog entries.

## Inmanta-dashboard: release 3.8.0 (2021-10-18)

### New features

- Extend proxy support (Issue #130)

## web-console: release 1.9.0
This component has had no new releases since the last product version.


# Release 2021.2.1 (2021-06-01)

## Inmanta-core: release 5.1.1 (2021-06-01)

### Bug fixes

- Add upperbound to docstring-parser dependency so that pip install does not fail

## Inmanta-dashboard: release 3.7.0 (2021-06-01)

No changelog entries.


# Release 2021.2 (2021-05-05)

## Inmanta-core: release 5.1.0 (2021-05-05)

### New features

- Mark the stable API using a decorator (Issue #2414)
- More strictly validate the schema of the project.yml and module.yml file (Issue #2723)
- Updated db schema update mechanism to track all installed versions (Issue #2724)
- Add partial support for collection type parameters for GET methods (Issue #2775)
- Add changelog section to the documentation (Issue inmanta/irt#417)
- Added developer getting started guide
- Added experimental caching support to the compiler
- Improved Inmanta install guide for Debian
- Extended stable API documentation (Issue inmanta/inmanta-lsm#408)
- Added built-in performance micro-benchmark, to help diagnose performance issues
- Added ability to do `pip install inmanta-core[pytest-inmanta-extension]`

### Deprecation notes

- Deprecated yaml dictionary syntax for module requires

### Bug fixes

- Correctly describe in the documentation how version constraints can be set on module dependencies in the module.yml file (Issue #2723)
- Ensure that an error at agent startup time is properly logged. (Issue #2777)
- Fixed compiler issue on rescheduling of plugins breaking the cycle breaking (Issue #2787)
- Fixed compiler issue on cycle breaking (Issue #2811)
- Fixed typos in language.rst file
- Changed python versions in install doc

### Other notes

- To enable caching on the compiler, either set the config value `compiler.cache` in the `.inmanta` file
or pass the option `--experimental-cache` to `inmanta compile`


## Inmanta-dashboard: release 3.7.0 (2021-05-05)

No changelog entries.


# Release 2021.1 (2021-02-25)

## inmanta-core: 5.0.0 (2021-02-25)

### Bug fixes
- Fix broken order by (#2638)
- Report the Inmanta OSS product version correctly (#2622)
- Set PYTHONPATH so that all subprocesses also see packages in parent venv (#2650, #2747)
- Create virtual environments without pip and use the pip of the parent venv
- Correctly set `[:n]` as syntactic sugar for `[0:n]` instead of leaving lower unbound (#2689)

### New features
- Add installation procedure for el8 to installation documentation

# Release 2020.6 (2020-12-23)

## inmanta-core: 4.0.0 (2020-12-23)

### New features
- Add support to use a custom venv path in the Project class (#2466)
- Added more specific location information for attributes (#2481)
- Added plugin call anchors to support ctrl-clicking a plugin call (#1954)
- Added rpdb signal handler (#2170)
- Added pagination support on api calls for agent and agentproc (#2500)
- Added support to build RPMs for a python version different from Python3.6 (#1857)
- Added support for assigning `null` to relations with lower arity 0 (#2459)
- Added documentation on the core dashboard (inmanta/dashboard#63)
- Decouple the compiler version from the OSS product version (#2573)
- Show versions of all installed components when running `inmanta --version` (#2574)

### Bug fixes
- Fix broken links in the documentation (#2495)
- Fixed bug in serialization of Resource with Unknowns in collections (#2603)
- Fixed documentation of `install_mode`
- Ensure all running compilations are stopped when the server is stopped (#2508)
- Cleanup old entries in the agentprocess and agentinstance database tables (#2499)
- Ensure the compiler service takes into account the environment variables set on the system (#2413)
- Fix `--server_address` option on `inmanta export` (#2514)
- Handle failure in an event handler consistently for local and non-local agents (#2509)
- Fix for cross agent dependencies responding to unavailable resources (#2501)
- Handle JSON serialization errors in handler log messages (#1875)
- Fixed too restrictive typing (and coercing) of AttributeStateChange (#2540)
- Export command should raise exception on failure (#2487)

### Upgrade notes
- Ensure the database is backed up before executing an upgrade.

### Other notes
- The inmanta core package is renamed from `inmanta` to `inmanta-core` to allow for true semantic versioning
    starting at `4.0.0`. A new `inmanta` package is provided that includes `inmanta-core` and continues the
    `<year>.<minor>[.<patch>]` version schema.

# Release 2020.5 (2020-10-27)

## New features
- Added support for environment markers as described in PEP 508 to module requirements parsing (#2359)
- Added design guide to the documentation
- Improved error message when plugin loading fails to include original exception and location (#2385)
- Improved duplicate attributes error message (#2386)

## Bug fixes
- Fixed import loop when using `inmanta.execute.proxy` as entry point (#2341)
- Fixed import loop when using `inmanta.resources` as entry point (#2342)
- Clearing an environment with merged compile requests no longer fails (#2350)
- Fixed compiler bug (#2378)
- Fix "compile_data_json_file" referenced before assignment (#2361)
- Fix server-autorecompile-wait config option (#2262)
- Specify the supported values of the 'format' parameter of the OpenAPI endpoint explicitly (#2369)
- Fix version cli argument conflict (#2358)
- Don't remove resource independent parameters on version deletion (#2370)
- Enhance installation documentation (#2241, #2356, #2357)
- Ensure that a protected environment can't be decommissioned (#2376)
- Don't load all code on agent start (#2343)
- Allow empty body in else branch for if-else statement (#2375)
- Fixed export failure with null in dict (#2437)
- Fixed small documentation issues
- Only store single agent instance in database for each distinct instance to prevent database overflow when agent rapidly and
    repeatadly dis- and reconnects (#2394)

# Release 2020.4 (2020-09-08)

## New features
- Added merging of similar compile requests to the compile queue (#2137)
- Export all handler's / resource's module's plugin source files so helper functions can be used from sibling modules (#2162, #2312)
- Added documentation on how a string is matched against a regex defined in a regex-based typedef (#2214)
- Added API to query ResourceActions
- Added support to query the resource action log of a resource via the CLI (#2253)
- Added conditional expression to the language with syntax condition ? x: y (#1987)
- Add support for inmanta-cli click plugins
- Added link to the PDF version of the documentation
- Added environment setting for agent_trigger_method (#2025)
- Expose compile data as exported by `inmanta compile --export-compile-data` via API (inmanta/inmanta-telco#54, #2317)
- Added `typedmethod` decorator `strict_typing` parameter to  allow `Any` types for those few cases where it's required (#2301)
- Added API method for halting all environment operations (#2228)

## Upgrade notes
- Ensure the database is backed up before executing an upgrade.
- Option `inmanta compile --json` is renamed to `inmanta compile --export-compile-data`
- `DynamicProxy.__getattr__` now raises an `AttributeError` instead of a plain `NotFoundException` when an attribute can not be
    found, for compatibility with Python's builtin `hasattr`. This change is backwards compatible, though it is recommended to
    except on `AttributeError` over `NotFoundException`. (#2991)

## Bug fixes
- Restore support to pass mocking information to the compiler
- Disallow parameters mapped to a header to be passed via the body instead (#2151)
- Handle skipped and unavailable as failures when calculating increments (#2184)
- Constrain agent name to string values (#2172)
- Fix for allowing comments in the requirements.txt file of modules (#2206)
- Allow equality checks between types to support optional value overrides (#2243)
- Don't add path params as query params to the url in the client (#2246)
- Allow Optional as return type for typedmethods (#2277)
- Made Dict- and SequenceProxy serializable to allow exporter to wrap dict and list attributes in other data structures (#2121)
- Improved reporting of `PluginException` (#2304)

# Release 2020.3 (2020-07-02)

## New features
- Added cleanup mechanism of old compile reports (#2054)
- Added `compiler.json` option and `--json` compile flag to export structured compile data such as occurred errors (#1206)
- Added troubleshooting documentation (#1211)
- Documentation on compiler API and JSON (#2060)
- Documentation on valid client types (#2015)
- Improved documentation on handler development (#1278)
- Added further documentation to inmanta-cli command (#2057)
- Documentation of config option types (#2072)
- Added method names as Operation Id to OpenApi definition (#2053)
- Added documentation of exceptions to the platform developers guide (#1210)
- Extended documentation of autostarted agent settings (#2040)
- Typing Improvements
- Redirect stdout and stderr to /var/log/inmanta/agent.{out,err} for agent service (#2091)
- Added resource name to log lines in agent log.
- Better reporting of json decoding errors on requests (#2107)
- Faster recovery of agent sessions
- Add compiler entrypoint to get types and scopes (#2114)
- Add support to push facts via the handler context (#593)

## Upgrade notes
- Ensure the database is backed up before executing an upgrade.
- Updated Attribute.get_type() to return the full type instead of just the base type (inmanta/inmanta-sphinx#29)
- Overriding parent attribute type with the same base type but different modifiers (e.g. override `number` with `number[]`)
    is no longer allowed. This was previously possible due to bug (#2132)

## Bug fixes
- Various small issues (#2134)
- Fixed issue of autostarted agents not being restarted on environment setting change (#2049)
- Log primary for agent correctly in the database when pausing/unpausing agents (#2079)
- Cancel scheduled deploy operations of an agent when that agent is paused (#2077)
- Fix agent-names config type (#2071)
- Ensure the internal agent is always present in the autostart_agent_map of auto-started agents (#2101)
- Cancel scheduled ResourceActions when AgentInstance is stopped (#2106)
- Decoding of REST return value for content type html with utf-8 charset (#2074)
- Empty list option in config no longer interpreted as list of empty string (#2097)
- Correct closing of agentcache
- Agent cross environment communication bug (#2163)
- Fixed an issue where an argument missing from a request would result in a http-500 error instead of 400 (#2152)
- Ensure agent is in proper state after URI change (#2138)
- Removed warning about collecting requirements for project that has not been loaded completely on initial compile (#2125)

# v 2020.2 (2020-04-24) Changes in this release:

## Breaking changes
- Non-boolean arguments to boolean operators are no longer allowed, this was previously possible due to bug (#1808)
- Server will no longer start if the database schema is for a newer version (#1878)
- The environment setting autostart_agent_map should always contain an entry for the agent "internal" (#1839)

## Deprecated
 - Leaving a nullable attribute unassigned now produces a deprecation warning. Explicitly assign null instead. (#1775)
 - Default constructors (typedef MyType as SomeEntityType(some_field = "some_value")). Use inheritance instead. (#402)
 - Old relation syntax (A aa [0:] -- [0:] B bb) (#2000)

## Fixed
 - Various compiler error reporting improvements (#1810, #1920)
 - Fixed cache leak in agent when deployments are canceled (#1883)
 - Improved robustness of modules update (#1885)
 - Removed environmental variables from agent report (#1891)
 - Use asyncio subprocess instead of tornado subprocess (#1792)
 - Added warning for incorrect database migration script names (#1912)
 - Agent manager remains consistent when the database connection is lost (#1893)
 - Ensure correct version is used in api docs (#1994)
 - Fixed double assignment error resulting from combining constructor kwargs with default values (#2003)
 - Fixed recursive unwrapping of dict return values from plugins (#2004)
 - Resource action update is now performed in a single transaction, eliminating the possibility of inconsistent state (#1944)
 - Type.type_string is now defined as returning the representation of the type in the inmanta DSL (inmanta/lsm#75)

## Added
 - Experimental data trace, root cause and graphic data flow visualization applications (#1820, #1831, #1821, #1822)
 - Warning when shadowing variable (#1366, #1918)
 - Added support for compiler warnings (#1779, #1905, #1906)
 - Added support for DISABLED flag for database migration scripts (#1913)
 - Added v5 database migration script (#1914)
 - Added support for declaring implement using parents together with normal implement declaration list (#1971)
 - Resource Action Log now includes timestamps (#1496)
 - Added support to pause an agent (#1128)
 - Added --no-tag option to module tool (#1939)
 - Added base exception for plugins and corresponding documentation (#1205)
 - Added tags to openapi definition (#1751)
 - Added support to pause an agent (#1128, #1982)
 - Plugins are now imported in the inmanta_plugins package to allow importing submodules (#507)
 - Added event listener to Environment Service (#1996)
 - Autostarted agents can load a new value for the autostart_agent_map setting without agent restart (#1839)
 - Added protected environment option (#1997)
 - Added warning when trying to override a built-in type with a typedef (#81)
 - Added inmanta-cli documentation to the docs (#1992)

# v 2020.1 (2020-02-19) Changes in this release:

## Fixed
 - Added support for conditions as expressions and vice versa (#1815)

## Breaking changes
- Entity instances are no longer allowed in list and dict attributes, this was previously possible due to bug (#1435)

## Fixed
 - Fixed incorrect parsing of booleans as conditions (#1804)
 - Added support for nullable types in plugins (#674)
 - Inmanta type module cleanup and type coverage
 - Various compiler error reporting improvements (#1584, #1341, #1600, #1292, #1652, #1221, #1707, #1480, #1767, #1766, #1762, #1575)
 - CRUDHandler bugfix, ensure update is not called on purged resources
 - Changes in default values: AUTO_DEPLOY, PUSH_ON_AUTO_DEPLOY are enabled by default,
 AGENT_TRIGGER_METHOD_ON_AUTO_DEPLOY is set to incremental deployment
 - Fixed deadlock triggered by std::AgenConfigHandler (#1662)
 - Removed the resourceversionid table from the database (#1627)
 - Remote machines not being available or not having a python interpreter now results in a clearer error.
 - Parse comments and urls correctly from the requirements.txt file of an Inmanta module (#1764)

## Added
 - Added support for dict lookup in conditions (#1573)
 - Added support for type casts for primitive types (#1798)
 - Added support for multiline string interpolations (#1568)
 - Added int type to the language (#1568)
 - Add get_environment_id to exporter (#1683)
 - Added inmanta-cli environment save command (#1666)
 - Added finalizer support to @cache annotation
 - Added support to parse the docstring of an entity
 - Added support for \*\*dict as kwargs for constructor calls and index lookups (#620, #1702)
 - Added support for kwargs in plugin calls, as named arguments as well as using \*\*dict (#1143)

## Removed
 - Removed the inmanta module validate command. Use pytest-inmanta fixtures to test your modules instead.
 - Removed Forms functionality (#1667)

# v 2019.5 (2019-12-05) Changes in this release:

## Fixed
 - Compiler bugfix, ensure done nodes are correctly removed from zerowaiters
 - Fixed memory leak in database layer
 - Fixed lexing of strings ending in an escaped backslash (#1601)
 - Fixed bug where `module freeze` results in empty module.yml (#1598)
 - Fixed inconsistent behavior of `export` and `export -j` (#1595)

IMPORTANT CHANGES:
 - Added environment variables for config, env variables overwrite all other forms of config (#1507)

v 2019.4 (2019-10-30) Changes in this release:
- Various bugfixes (#1367,#1398,#736, #1454)
- Added if statement (#1325)
- Added CORS Access-Control-Allow-Origin header configuration (#1306)
- Added --version option (#1291)
- Added retry to moduletool update, to allow updating of corrupt projects (#177)
- RPM-based installations on Fedora are not supported anymore
- Added option to configure asyncpg pool (#1304)
- Split out the main service into many smaller services (#1388)
- Use python3 from the core OS in Dockerfile
- Introduce v2 protocol and implement project and environment api in v2 (#1412)
- Improve agent documentation (#1389)
- Improve language reference documentation (#1419)
- Change autostart_agent_deploy_splay_time from 600 to 10 (#1447)
- Introduce the bind-address and bind-port config option (#1442)
- Switch to sequential version numbers instead of timestamps (#1011)
- Fixed memory leak in TaskHandler
- Don't install packages inherited from the parent virtualenv
- Added logging to CRUD methods of handler and a diff method with context
- HTTP errors are logged at DEBUG level only (#1282)
- Verify hashes when serving a file (#532)
- Mark resource as failed when code loading fails (#1520)
- Print extra env variables in init log and only store those in database (#1482)
- Add feature manager for enabling and disabling orchestrator features (#1530)
- Add get_environment_id to plugin context (#1331)
- Log server bind address and bind port on startup (#1475)
- Fix warning about transport config (#1203)
- Add setting to environment to disable purge on delete (#1546)

IMPORTANT CHANGES:
- Older compiler versions are no longer supported with this server
- The Inmanta server now listens on 127.0.0.1:8888 by default, while
  this was 0.0.0.0:8888 in previous versions. This behavior is
  configurable with the `bind-address` config option.

DEPRECATIONS:
- The `server_rest_transport.port` config option is deprecated in favor
  of the `server.bind-port` option.

v 2019.3 (2019-09-05) Changes in this release:
- Various bugfixes (#1148, #1157, #1163, #1167, #1188)
- Abort server startup if the database can not be reached (#1153)
- Use native coroutines everywhere (async def)
- Updated dockerfile and docker-compose to use postgres and centos
- Added extensions mechanism (#565, #1185)
- Add /serverstatus api call to get version info, loaded slices and extensions (#1184)
- Support to set environment variables on the Inmanta server and its agents
- Split of server recompile into separate server slice (#1183)
- Add API to inspect compiler service queue (#1252)
- Define explicit path in protocol methods
- Added support for schema management for multiple slices in the same database (#1207)
- Marked pypi package as typed
- Create pytest-inmanta-extensions package for extensions testing
- Added support for /etc/inmanta/inmanta.d style configuration files (#183)
- Increased the iteration limit to 10000. This value is controlled with INMANTA_MAX_ITERATIONS
  environment variable.
- Added support for custom resource deserialization by adding the 'populate' method
- Improve compiler scaling by using more efficient data structures
- Added the --export-plugin option to the export command (#1277)
- Only one of set_created, set_updated or set_purged may be called now from a handler
- Remove facts when the resource is no longer present in any version (#1027)
- Successful exports without resources or unknowns will now be exported
- Export plugins will not run when the compile has failed
- Documentation updates and improvements (#1209)

DEPRECATIONS:
* The files /etc/inmanta/agent.cfg and /etc/inmanta/server.cfg are not used anymore. More information about the available
configuration files can be found in the documentation pages under `Administrator Documentation -> Configuration files`.

v 2019.2 (2019-04-30)
Changes in this release:
- Various bugfixes (#1046, #968, #1045)
- Migration from mongodb to postgres (#1023, #1024, #1025, #1030)
- Added metering using pyformance
- Added influxdb reporter for protocol endpoint metrics
- Remove the configuration option agent-run-at-start (#1055)
- Add project id and environment id as optional parameters to API call (#1001)
- Fixed an issue which cleared the environment on remote python 2 interpreters
- Improve deploy command resilience and added option to work with dashboard
- Added API endpoint to trigger agents deploy (#1052)
- Documentation updates and improvements (#905)

v 2019.1 (2019-03-06)
Changes in this release:
- Various bugfixes and performance enhancements (#873, #772, #958, #959, #955)
- Dependency updates
- Introduce incremental deploy (#791, #794, #793, #792, #932, #795)
- Introduce deploying resource state (#931)
- Introduce request_timeout option for transport settings
- Add support to run the compiler on windows
- Add exception explainer to compiler for 'modified after freeze' (#876)
- Improve log format, added replace file name with logger name
- Split out logs, stdout and stderr in autostarted agents (#824, #234)
- Add logging of resource actions on the server and purging of resource actions in the database (#533)
- Improve agent logging
- Replace virtualenv by python standard venv (#783)
- Update to Tornado 5, moving from tornado ioloop to the standard python async framework (#765)
- Use urllib client for fetching jwks public keys
- Remove all io_loop references and only use current ioloop (#847)
- Remove environment directory from server when environment is removed (#838)
- Catch various silent test failures
- Extend mypy type annotations
- Port unit tests to pytest-asyncio and fix deprecation warnings (#743)
- Raise exception on bad export to make inmanta export fail with exit status > 0
- Refactor protocol
- Improve lazy execution for attributes
- Update autogenerated config file for agents with correct server hostname (#892)

DEPRECATIONS:
- Minimal python version is now python 3.6
- Removal of snapshot and restore functionality from the server (#789)
- Removed the non-version api (#526)
- The config option agent-interval, agent-splay, autostart_agent_interval and autostart_splay are
deprecated in favour of agent-deploy-interval, agent-deploy-splay-time, autostart_agent_deploy_interval
and autostart_agent_deploy_splay_time respectively. The deprecated options will be removed in release 2019.2

v 2018.3 (2018-12-07)
Changes in this release:
- Various bugfixes and performance enhancements
- Dependency updates
- Added improved error reporting to CLI (#814)
- Fixed missing re-raise on pip install  (#810)
- Add pytest plugins (#786)
- Extra test cases for the data module + two bugfixes (#805)
- Fix deprecation warnings (#785)
- Reorganized test case in more modules to reduce the number of merge conflicts (#764)
- Prevent purge_on_delete due to failed compile (#780)
- Add mypy to tox and improve typing annotations (no enforcement yet) (#763)
- Removed incorrect uninitialize of subprocess signal handler (#778, #777)
- Fix modules do command (#760)
- Changed process_events so that it is called even when processing a skip. (#761)
- Track all locations where an instance has been created. (fixes #747)
- Add start to the index for the get_log query (#758)
- Improved reporting of nested exceptions (#746)
- Added compiler check on index attributes so an index on a nullable attribute now raises a compiler error. (#745)
- Added support for lazy attribute execution in constructors (#729)
- Big update to module and project version freeze. See documentation for more details (#106)
- Added argument to @plugin to allow unknown objects as arguments (#754)
- Fix for deploy of undefined resource (#627)
- Improved handling ofr dryrun failures (#631)
- Correctly store and report empty facts (#731)
- Allow get facts from undeployed or undefined resources  (#726)
- Minor changes for ide alpha release (#607)
- Added uniqueness check to indices (#715)
- Bugfixes in handling of optional attributes (#724)
- Transport cleanup (added bootloader, split off session management) (#564)
- Reserved keywords in resources (#645)
- Fix a bug in option definition
- Use own mongobox implementation that works with mongo >= 4
- Fixed reporting on undefined list attributes (#657)
- Improved list freeze for gradual execution (#643)
- Fixed bug in bounds check (#671)
- Improved error reporting on bad assignment (#670)
- Improved error reporting on missing type (#672)
- Added in operator for dicts (#673)

v 2018.2 (2018-07-30)
Changes in this release:
- Various bugfixes and performance enhancements
- Dependency updates
- The internal storage format for code is optimized. This introduces API and schema changes.
  This release supports both storage versions. The old version will be removed in the next release.
- Support formatter in repo url
- Make export of complete model configurable
- Use id of loopvar instead of hash to support iteration over list returned by plugins
- Fix error in default args for list attribute (#633)
- Add multi level map lookup (#622 and #632)
- Improved deploy, make deploy sync
- Added improved error message for lower bound violations on relations (#610)
- Fixes for empty optionals  (#609)
- Added improved logging to context handler (#602)
- Added fix for string representation (#552)
- Added support for single quotes (#589)
- Fix in operator in typedefs (#596)
- Fixed line numbers on MLS (#601)
- Added += operator for assignment to lists (#587)
- Add a synchronous protocol client
- Fix error message for wrong type in ctor
- Improve index error reporting
- Fix validate on modules with no commited version
- Set purged=false on clone in CRUDHandler (#582)
- Add gzip encoding support to protocol (#576)
- added anchormap functions to compiler
- Improved error reporting on for loops (#553)

v 2018.1 (2018-02-09)
Changes in this release:
- Various bugfixes and performance enhancements
- Dependency updates
- Ubuntu 14.04 mongo (2.4) is no longer supported. Version 2.6 or higher is required.
- The inmanta API endpoint is now versioned and available under /api/v1. The old API methods
  still work, but are deprecated and will be removed in the next release.
- Added support for escapes in regex (#540)
- Added per env config for agent_interval (#542): This adds an per environment setting that controls
  the agent interval for the agents started by the server.
- Removed implicit string to number conversion (#539)
- Fix dockerfile (#538)
- Fixed execnet resource leak (#534)
- Solution for resource leak issue in agent (#518): Numerous stability fixes for the agent related
  to resource leaks and races
- Remove compile reports on env clean
- Refactor report API: The report list no longer contains the output of the processes. This
  reduces the size of the response.
- Fix recompile triggered from a form change
- Add missing mongo indexes to improve performance
- Remove catchlog from tox run
- Create a post method for notify: only the post method allows to pass metadata
- Fix trigger metadata (#520): Add compile metadata to each version. Fixes #519 and add delete with
  resource_id for parameters
- Add representation for null value

v 2017.4 (2017-11-27)
Changes in this release:
- Various bugfixes and performance enhancements
- Dependency updates
- added keyword parents, and implemented implementation inheritance (#504)
- set_param recompile parameter
- Raise an exception when duplicate resources are exported (#513)
- Added fix for index issue (#512)
- Allow to configure server compile per environment
- Add remove parameter API call
- Attributes and lists now accept trailing comma (#502)
- Added check for attribute redefinition within one entity (#503)
- Parse bool values in the rest api
- Fix bug in dryrun reporting with auth enabled

v 2017.3 (2017-10-27)
Changes in this release:
- Various bugfixes and performance enhancements
- Dependency updates
- Add relation annotations to the relation attribute and resolve it for exporters to use
- Documentation improvements
- Add an undefined resource state to the server (#489)
  Previously all unknown handling was done in the server. This resulted in strange reporting as the number of managed resource
  could go up and down. Now, an additional resource state "undefined" is introduced. This  state is handled similar to skipped
  during deploys. Undefined resources are undeployable.
- Undeployable resources are now already marked as finished at the moment a version is released or a dryrun is requested.
  Resources that depend on resources in an undeployable state will be skipped on the server as well.
- Sort index attributes: This patch ensure that std::File(host, path) and std::File(path, host) are the same indexes.
- Improved modules list ouput: rename columns and added a column to indicate matching rows
- Improve attribute check. fixes (#487)
- Fix index issues related with inheritance (#488)
- When a resource is purged, its facts will be removed. (#3)
- Add location to type not found exception in relation (#475. #294)
- Add JWT authz and limitation to env and client type (#473)
- Added fix for function execution in constraints (#470)
- Each agent instance now has its own threadpool to execute handlers. (#461)
- Allow agent instances to operate independently (#483)
- Improved error reporting on parser errors (#468, #466)
- Fixed selection of lazy arguments (#465)

v 2017.2 (2017-08-28)
Changes in this release:
- Various bugfixes and performance enhancements
- Dependency updates
- Preserve env variables when using sudo in the agent
- Prune all versions instead of only the ones that have not been released.
- Use python 2.6 compatible syntax for the remote io in the agent
- Gradual execution for for-loops and constructors
- Stop agents and expire session on clear environment
- Improve purge_on_delete semantics
- New autostart mechanism  (#437)
- Add settings mechanism to environment. More settings will become environment specific in later
  releases.
- Do not create index in background to prevent race conditions
- Add support for exception to the json serializer
- Invert requires for purged resources (purge_on_delete)
- Add autodeploy_splay option
- Remove ruaml yaml dependency (#292)
- Handle modified_count is None for mongodb < 2.6
- Add python3.6 support
- Add nulable types
- Various documentation updates
- Added monitor command to inmanta-cli (#418)
- Generate inmanta entrypoint with setuptools
- Update quickstart to use centos
- Improve event mechanism (#416)
- Added auto newline at end of file (#413)
- Improved type annotations for plugins and improved object unwrapping (#412)
- Inline index lookup syntax (#411)
- Added cycle detection (#401)
- Fixed handling of newlines in MLS lexer mode (#392)
- Added docstring to relations, typedef, implementation and implement (#386)
- Fix agent-map propagation from deploy

v 2017.1 (2017-03-29)
New release with many improvements and bug fixes. Most noteable features include:
- Port CLI tool to click and improve it. This removes cliff and other openstack deps from core
- Complete rewrite of the database layer removing the dependency on motorengine and improve
  scalability.
- Cleanup of many API calls and made them more consistent
- Improved handler protocol and logging to the server.

v 2016.6 (2017-01-08)
Mainly a bugfix and stabilisation release. No new features.

v 2016.5 (2016-11-28)
New release with upgraded server-agent protocol
- Upgraded server agent protocol
- New relation syntax

v 2016.4 (2016-09-05)
New relase of the core platform
- Various compiler improvements
- Add list types
- Cleanup of is defined syntax in the DSL and templates
- Many additional test cases
- Various bugfixes

v 2016.3 (2016-08-18)
New release. Way to late due to kids and vacation.
- Added SSL support
- Added auth to server
- Add JIT loading of modules
- Various bug fixes

v 2016.2.3 (2016-05-30)
- Fix memory leak in server

v 2016.2.2 (2016-05-25)
- Remove urllib3 dependency to ease packaging on el7

v 2016.2.1 (2016-05-04)
- Various bugfixes related to new ODM and async IO

v 2016.2 (2016-05-02)
- First bi-monthly release of Inmanta
- New compiler that speeds up compilation an order of magnitude
- All RPC is now async on the tornado IOLoop
- New async ODM for MongoDB
- Increased test coverage
