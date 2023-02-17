# Release 2023.1.1 (2023-02-17)

## Upgrade notes

- Ensure the database is backed up before executing an upgrade.

## Inmanta-core: release 8.2.0 (2023-02-09)

### Improvements

- Support `inmanta module release` options `-c`, `--patch`, `--minor`, `--major` without `--dev`

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
