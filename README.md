# FastAPI + SQLAlchemy + Okta + Oso example app

This is an example app that demonstrates using Okta and Oso to add
authentication and authorization to a FastAPI + SQLAlchemy application. Please
read [the accompanying post on Okta's developer blog][Okta blog] to learn how it
was created.

The `main` branch has authentication (but no authorization), and the
`authorized` branch adds authorization. [Compare the two branches][] to view the
delta of adding authorization to the app.

## Prerequisites

- [Okta CLI][]
- Python 3.6 or later
- A recent version of [Node.js][].

[Okta blog]: https://developer.okta.com/blog/2021/06/23/okta-oso-fastapi-sqlalchemy
[Compare the two branches]: https://github.com/osohq/fastapi-sqlalchemy-okta-oso-example/compare/authorized
[Okta CLI]: https://github.com/okta/okta-cli
[Node.js]: https://nodejs.org/
