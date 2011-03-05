# $Id:$

# port and ip to bind
PORT=8000
IP=0.0.0.0

# custom definitions
-include Makefile.def
-include $(SETTINGS)


# constants
ENV_DEFAULT_NAME=.env
VIRTUALENV=virtualenv
DEFAULT_APP=project
MANAGE=python $(app)/manage.py
TARGET_BRANCH=$(deploy_branch)
TARGET=$(deploy_app)
DEPLOYMENT_MODE=$(deploy_mode)
TOOLS=tools

DEPLOYMENT_DIR=.deployment

# definitions
JS_LIB_DIR=./$(app)/static_media/js/lib
CSS_LIB_DIR=./$(app)/static_media/css/lib

# auto definitions
ifndef PYTHON
	PYTHON=$(shell type -p python)
endif

ifndef VIRTUALENV
	VIRTUALENV=$(shell type -p virtualenv)
endif


# Targets
.PHONY: test clean todo docs project

test: clean nosetests
fasttest: clean nosetests_fast

nosetests:
	$(MAKE) -C $(app) build test

nosetests_fast:
	$(MAKE) -C $(app) build nosetests_fast

clean:
	-[ -d db ] && $(MAKE) -C db clean
	$(MAKE) -C $(app) clean
	-rm *~*
	-find . -name '*.pyc' -exec rm {} \;

deploy:
	ssh $(deploy_user)@$(deploy_target) 'bash -s' < $(DEPLOYMENT_DIR)/$(DEPLOYMENT_MODE) $(TARGET) $(TARGET_BRANCH)

virtualenv:
	echo "Creating virtualenv in $(ENV_DEFAULT_NAME)";\
	$(VIRTUALENV) -p $(PYTHON) --no-site-packages $(ENV_DEFAULT_NAME);\
	$(ENV_DEFAULT_NAME)/bin/pip install -r requirements.txt;\

	echo Updating .venv file for current virtual environment
	echo "VIRTUALENV_PATH=$(ENV_DEFAULT_NAME)" > .venv;

	@echo Install requirements
	-source ./$(ENV_DEFAULT_NAME)/bin/activate && ./$(ENV_DEFAULT_NAME)/bin/easy_install pip
	-source ./$(ENV_DEFAULT_NAME)/bin/activate && ./$(ENV_DEFAULT_NAME)/bin/pip install -r requirements.txt

project:
	@echo Generating default settings
	@(for orig_file in `ls Makefile.*.sample`; do\
		[[ -z "$(PROJECT_USER)" ]] && PROJECT_USER="$(PROJECT)";\
		dest_file=`echo "$${orig_file}" | awk -F. '{printf("%s.%s", $$1, $$2)}'`; \
		cat $${orig_file} | \
			sed 's/%PROJECT%/$(PROJECT)/g' | \
			sed "s/%PROJECT_USER%/$${PROJECT_USER}/g" \
			> $${dest_file};\
	done );

	@echo Rename default application to active: $(DEFAULT_APP) to $(PROJECT)
	-mv $(DEFAULT_APP) $(PROJECT)

install: virtualenv
	@echo Add required libraries
	-git submodule add git://github.com/ry/node.git $(JS_LIB_DIR)/node
	-git submodule add git://github.com/jquery/jquery.git $(JS_LIB_DIR)/jquery
	-git submodule add git://github.com/agarzola/jQueryAutocompletePlugin.git $(JS_LIB_DIR)/jquery.autocomplete
	-git submodule add git://github.com/malsup/form.git $(JS_LIB_DIR)/jquery.form
	
	@echo Refresh submodules
	-git submodule update
	
	@echo Building Node.js
	cd $(JS_LIB_DIR)/node && ./configure --prefix=./build;
	$(MAKE) -C $(JS_LIB_DIR)/node;
	$(MAKE) -C $(JS_LIB_DIR)/node install;
	
	@echo Building jquery.min.js
	-$(MAKE) -C $(JS_LIB_DIR)/jquery init
	-$(MAKE) -C $(JS_LIB_DIR)/jquery -e JS_ENGINE=../node/build/bin/node min
	-cp $(JS_LIB_DIR)/jquery/dist/jquery.min.js $(JS_LIB_DIR)/

	@echo Building jquery libs
	-cp $(JS_LIB_DIR)/jquery.autocomplete/jquery.autocomplete.min.js $(JS_LIB_DIR)/
	-cp $(JS_LIB_DIR)/jquery.autocomplete/jquery.autocomplete.css $(CSS_LIB_DIR)/
	-java -jar $(TOOLS)/yuicompressor-2.4.4.jar --nomunge -o $(JS_LIB_DIR)/jquery.form.min.js $(JS_LIB_DIR)/jquery.form/jquery.form.js

todo:
	find . -type f -not -name '*~*' -not -name 'Makefile*' -print0 | xargs -0 -e grep -n -e 'todo'

fresh_syncdb:
	-rm $(app).db
	$(MANAGE) syncdb --noinput --settings=$(settings)

syncdb:
	$(MANAGE) syncdb --noinput --settings=$(settings)
	$(MANAGE) loaddata initial_data.json --settings=$(settings)

shell:
	$(MANAGE) shell_plus --settings=$(settings)

dbshell:
	$(MANAGE) dbshell --settings=$(settings)

run:
	$(MANAGE) runserver $(IP):$(PORT) --settings=$(settings)

manage:
	$(MANAGE) $(CMD) --settings=$(settings)

migrate:
	$(MANAGE) schemamigration $(APP) --auto --settings=$(settings)
	$(MANAGE) migrate $(APP) --settings=$(settings)

help:
	cat README

### Local variables: ***
### compile-command:"make" ***
### tab-width: 2 ***
### End: ***
