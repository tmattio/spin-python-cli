(name python-cli)
(description "Python Command Line Interface")

(config project_name
  (input (prompt "Project name")))

(config project_slug
  (input (prompt "Project slug"))
  (default (slugify :project_name))
  (rules
    ("The project slug must be lowercase and contain ASCII characters and '-' only."
      (eq :project_slug (slugify :project_slug)))))

(config project_snake
  (default (snake_case :project_slug)))

(config project_description
  (input (prompt "Description"))
  (default "A short, but powerful statement about your project"))

(config username
  (input (prompt "Name of the author")))

(config github_username
  (input (prompt "Github username"))
  (default :username))

(config ci_cd
  (select
    (prompt "Which CI/CD do you use")
    (values Github None))
  (default Github))

(ignore
  (files github/*)
  (enabled_if (neq :ci_cd Github)))

(post_gen
  (actions 
    (run python -m pip install --upgrade pipenv)
    (run make install))
  (message "🎁  Installing dependencies. This might take a couple minutes."))

(example_commands
  (commands
    ("make lint" "Lint the code.")
    ("make docs" "Generate the documentation.")
    ("make test" "Starts the test runner.")))
