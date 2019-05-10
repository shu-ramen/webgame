import React from 'react';
import ReactDOM from 'react-dom';
import { Row, Col, Alert, Container, Form, Button } from 'react-bootstrap';

class Login extends React.Component {
    constructor() {
        super();
    }

    getFormErrorTag(formError) {
        if (formError) {
            return (
                <Row>
                    <Col xl={12} lg={12} md={12} sm={12} sx={12}>
                        <Alert variant="danger">Your username and password didn't match. Please try again.</Alert>
                    </Col>
                </Row>
            );
        }
        else {
            return "";
        }
    }

    getNextErrorTag(hasNext, authenticated) {
        if (hasNext) {
            if (authenticated) {
                return (
                    <Row>
                        <Col xl={12} lg={12} md={12} sm={12} sx={12}>
                            <Alert variant="danger">Your account doesn't have access to this page. To proceed, please login with an account that has access.</Alert>
                        </Col>
                    </Row>
                );
            }
            else {
                return (
                    <Row>
                        <Col xl={12} lg={12} md={12} sm={12} sx={12}>
                            <Alert variant="danger">Please login to see this page.</Alert>
                        </Col>
                    </Row>
                );
            }
        }
        else {
            return "";
        }
    }

    getCsrfTokenTag() {
        let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        return (
            <input type="hidden" name="csrfmiddlewaretoken" value={csrfToken}></input>
        )
    }

    getNextTag() {
        let next = document.getElementsByName("next")[0].value;
        return (
            <input type="hidden" name="next" value={next}></input>
        )
    }

    render() {
        let formErrorTag = this.getFormErrorTag(this.props.formError);
        let nextErrorTag = this.getNextErrorTag(this.props.hasNext, this.props.authenticated);
        let csrfTokenTag = this.getCsrfTokenTag();
        let nextTag = this.getNextTag();

        return (
            <Container>
                <br />
                <Row>
                    <Col></Col>
                    <Col xl={8} lg={8} md={8} sm={12} sx={12}>
                        {formErrorTag}
                        {nextErrorTag}
                        <Form method="POST" action="/accounts/login/">
                            {csrfTokenTag}
                            <Form.Group controlId="id_username">
                                <Form.Label>Username</Form.Label>
                                <Form.Control name="username"  type="text" placeholder="Enter username" required />
                            </Form.Group>
                            <Form.Group controlId="id_password">
                                <Form.Label>Password</Form.Label>
                                <Form.Control name="password" type="password" placeholder="Enter password" required />
                            </Form.Group>
                            <Button variant="primary" size="lg"  type="submit" block>Log in</Button>
                            <Button variant="link" href="/accounts/signup/" block>Create new account</Button>
                            {nextTag}
                        </Form>
                    </Col>
                    <Col></Col>
                </Row>
            </Container>
        )
    }
}

class Error extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col></Col>
                    <Col xl={8} lg={8} md={8} sm={12} sx={12}>
                        <Alert variant="danger">{this.props.error}</Alert>
                    </Col>
                    <Col></Col>
                </Row>
            </Container>
        )
    }
}

if (document.getElementById('formerror-hasnext-authenticated-login') != null) {
    ReactDOM.render(<Login formError={true} hasNext={true} authenticated={true} />, document.getElementById('formerror-hasnext-authenticated-login'))
}

if (document.getElementById('hasnext-authenticated-login') != null) {
    ReactDOM.render(<Login formError={false} hasNext={true} authenticated={true} />, document.getElementById('hasnext-authenticated-login'))
}

if (document.getElementById('formerror-hasnext-not-authenticated-login') != null) {
    ReactDOM.render(<Login formError={true} hasNext={true} authenticated={false} />, document.getElementById('formerror-hasnext-not-authenticated-login'))
}

if (document.getElementById('hasnext-not-authenticated-login') != null) {
    ReactDOM.render(<Login formError={false} hasNext={true} authenticated={false} />, document.getElementById('hasnext-not-authenticated-login'))
}

if (document.getElementById('formerror-authenticated-login') != null) {
    ReactDOM.render(<Login formError={true} hasNext={false} authenticated={true} />, document.getElementById('formerror-authenticated-login'))
}

if (document.getElementById('authenticated-login') != null) {
    ReactDOM.render(<Login formError={false} hasNext={false} authenticated={true} />, document.getElementById('authenticated-login'))
}

if (document.getElementById('formerror-not-authenticated-login') != null) {
    ReactDOM.render(<Login formError={true} hasNext={false} authenticated={false} />, document.getElementById('formerror-not-authenticated-login'))
}

if (document.getElementById('not-authenticated-login') != null) {
    ReactDOM.render(<Login formError={false} hasNext={false} authenticated={false} />, document.getElementById('not-authenticated-login'))
}