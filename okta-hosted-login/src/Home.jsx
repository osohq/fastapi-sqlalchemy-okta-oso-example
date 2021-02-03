/*
 * Copyright (c) 2018, Okta, Inc. and/or its affiliates. All rights reserved.
 * The Okta software accompanied by this notice is provided pursuant to the Apache License, Version 2.0 (the "License.")
 *
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *
 * See the License for the specific language governing permissions and limitations under the License.
 */

import { useOktaAuth } from '@okta/okta-react';
import React, { useState, useEffect } from 'react';
import { Button, Form, Header, Table } from 'semantic-ui-react';

const SERVER = 'http://localhost:8000/bears';

const Home = () => {
  const { authState, oktaAuth } = useOktaAuth();
  const [userInfo, setUserInfo] = useState(null);
  const [token, setToken] = useState(null);
  const [bears, setBears] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const [name, setName] = useState('');
  const [species, setSpecies] = useState(null);

  useEffect(() => {
    if (!authState.isAuthenticated) {
      // When user isn't authenticated, forget any user info
      setToken(null);
      setUserInfo(null);
    } else {
      setToken(oktaAuth.getAccessToken());
      oktaAuth.getUser().then((info) => {
        setUserInfo(info);
      });
    }
  }, [authState, oktaAuth]); // Update if authState changes

  // Fetch bears.
  useEffect(async () => {
    if (token) {
      const headers = { Authorization: `Bearer ${token}` };
      try {
        const res = await fetch(SERVER, { headers });
        if (res.status === 200) {
          const data = await res.json();
          setBears(data);
        } else {
          console.error(res.status, res.detail);
          setBears([]);
        }
      } catch (e) {
        console.error(e);
        setBears([]);
      }
    }
  }, [token, submitted]);

  // Create a new bear.
  useEffect(async () => {
    if (submitted) {
      if (!name || !species) {
        setSubmitted(false);
        return;
      }
      const headers = { Authorization: `Bearer ${token}` };
      setSubmitted(false);
      try {
        const body = JSON.stringify({ name, species });
        await fetch(SERVER, { headers, method: 'POST', body });
      } catch (e) {
        console.error(e);
      } finally {
        setName('');
        setSpecies(null);
      }
    }
  }, [submitted]);

  const login = async () => {
    oktaAuth.signInWithRedirect();
  };

  if (authState.isPending) {
    return (
      <div>Loading...</div>
    );
  }

  return (
    <div>
      <div>
        <Header as="h1">Bear Management Service</Header>

        { authState.isAuthenticated && !userInfo
        && <div>Loading...</div>}

        {authState.isAuthenticated && userInfo
        && (
        <div>
          <p>
            Welcome back,&nbsp;
            {userInfo.name}
            !
          </p>

          <Header as="h2">Create a new bear</Header>
          <Form onSubmit={() => setSubmitted(true)}>
            <Form.Group>
              <Form.Input
                placeholder="Name"
                name="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
              <Form.Select
                placeholder="Species"
                options={
                  ['black', 'brown', 'panda', 'polar', 'sloth', 'spectacled', 'sun']
                    .map((text) => ({ key: text, value: text, text }))
                }
                name="species"
                value={species}
                onChange={(e) => setSpecies(e.target.innerText)}
              />
              <Form.Button content="Submit" />
            </Form.Group>
          </Form>

          <Header as="h2">Bears</Header>
          <Table basic>
            <Table.Header>
              <Table.Row>
                <Table.HeaderCell>Name</Table.HeaderCell>
                <Table.HeaderCell>Species</Table.HeaderCell>
                <Table.HeaderCell>Owner</Table.HeaderCell>
              </Table.Row>
            </Table.Header>
            <Table.Body>
              {bears.map((bear) => (
                <Table.Row>
                  <Table.Cell>{bear.name}</Table.Cell>
                  <Table.Cell>{bear.species}</Table.Cell>
                  <Table.Cell>{bear.owner}</Table.Cell>
                </Table.Row>
              ))}
            </Table.Body>
          </Table>
        </div>
        )}

        {!authState.isAuthenticated
        && (
        <div>
          <Button id="login-button" primary onClick={login}>Login</Button>
        </div>
        )}

      </div>
    </div>
  );
};
export default Home;
