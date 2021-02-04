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

* An Okta Developer Account. You can sign up for one at
  https://developer.okta.com/signup/.
* An Okta Application configured for Single-Page App (SPA) mode. This is done
  from the Okta Developer Console. See the [OIDC SPA Setup Instructions][].
  When following the wizard, use the default properties. They are are designed
  to work with Okta's sample applications.

## Running This Example

First, install dependencies:

```bash
npm install
```

Now you need to gather the following information from the Okta Developer Console:

- **Client ID** - The client ID of the SPA application that you created
  earlier. This can be found on the "General" tab of an application, or the
  list of applications. This identifies the application that tokens will be
  minted for.
- **Issuer** - This is the URL of the authorization server that will perform
  authentication. All Developer Accounts have a "default" authorization server.
  The issuer is a combination of your Org URL (found in the upper right of the
  console home page) and `/oauth2/default`. For example,
  `https://dev-1234.okta.com/oauth2/default`.

Add your **Client ID** and **Issuer** to a file named `.env` in this directory.
[dotenv](https://www.npmjs.com/package/dotenv) will take care of exporting them
when you run the app. Once you're done, the `.env` file should look as follows:

```ini
CLIENT_ID=123xxxxx123
ISSUER=https://dev-1234.okta.com/oauth2/default
```

With variables set, start the app server:

```console
npm start
```

Now navigate to http://localhost:8080 in your browser.

If you see a home page that prompts you to login, things are working! Clicking
the **Log in** button will redirect you to the Okta hosted sign-in page.

You can login with the same account that you created when signing up for your
Developer Org, or you can use a known username and password from your Okta
Directory.

**Note:** If you are currently using the Okta Developer Console, you already
have a Single Sign-On (SSO) session for your Org. You will be automatically
logged into your application as the same user that is using the Developer
Console. You may want to use an incognito tab to test the flow from a blank
slate.

[okta-hosted-login]: https://github.com/okta/samples-js-react/tree/832523a10613e8a98f59b5520f47c8d424e9a08b/okta-hosted-login
[okta-hosted-login/README.md]: https://github.com/okta/samples-js-react/blob/832523a10613e8a98f59b5520f47c8d424e9a08b/okta-hosted-login/README.md
[OIDC SPA Setup Instructions]: https://developer.okta.com/docs/guides/sign-into-spa/react/before-you-begin
