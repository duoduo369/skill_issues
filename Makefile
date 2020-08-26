auto: update_gitbook build_gitbook

update_gitbook:
	python3 update_gitbook.py

build_gitbook:
	gitbook build

