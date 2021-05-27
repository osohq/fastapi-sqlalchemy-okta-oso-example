# Okta-secured front end app

This is a clone of
[okta/samples-js-react/tree/master/okta-hosted-login][okta-hosted-login] that's
been modified to serve as our front end app. This app handles user
authentication (via Okta) and then uses the "Access Token" returned from Okta
when making calls to our FastAPI- and SQLAlchemy-powered back end.

The below is copied from [the original][okta-hosted-login/README.md] with
slight modification.

## Prerequisites

Before running this sample, you will need the following:

* The [Okta CLI][] installed.
* A recent version of [Node.js][].

## Running This Example

For an in-depth walkthrough of this example app, please see [the accompanying
blog post on Okta's developer blog][Okta blog].

[okta-hosted-login]: https://github.com/okta/samples-js-react/tree/832523a10613e8a98f59b5520f47c8d424e9a08b/okta-hosted-login
[okta-hosted-login/README.md]: https://github.com/okta/samples-js-react/blob/832523a10613e8a98f59b5520f47c8d424e9a08b/okta-hosted-login/README.md
[Okta CLI]: https://github.com/okta/okta-cli
[Node.js]: https://nodejs.org/
[Okta blog]: https://developer.okta.com/blog/2021/05/28/using-okta-and-oso-to-secure-a-fastapi-and-sqlalchemy-app
