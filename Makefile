.PHONY: validate package bundle repository eval-prepare all

validate:
	python3 scripts/validate_repo.py

package: validate
	python3 scripts/package_skill.py

bundle: validate
	python3 scripts/build_generic_bundle.py

repository: validate
	python3 scripts/package_repository.py

eval-prepare: validate
	python3 scripts/eval_suite.py prepare

all: package bundle repository eval-prepare
