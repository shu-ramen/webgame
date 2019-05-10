import React from 'react';
import ReactDOM from 'react-dom';
import { Row, Col, Alert, Container, Form, Button } from 'react-bootstrap';

class LoggedOut extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Container>
                <br />
                <Row>
                    <Col></Col>
                    <Col xl={8} lg={8} md={8} sm={12} sx={12}>
                        <Row>
                            <Col xl={12} lg={12} md={12} sm={12} sx={12}>
                                <Alert variant="light">Thank you for your playing! See you again!</Alert>
                            </Col>
                        </Row>
                        <Row>
                            <Col xl={12} lg={12} md={12} sm={12} sx={12}>
                                <Button variant="primary" size="lg" href="/accounts/login/"  block>Log in</Button>
                            </Col>
                        </Row>
                        <Row>
                            <Col xl={12} lg={12} md={12} sm={12} sx={12}>
                                <Button variant="link" href="/accounts/signup/" block>Create new account</Button>
                            </Col>
                        </Row>
                    </Col>
                    <Col></Col>
                </Row>
            </Container>
        )
    }
}

ReactDOM.render(
    <LoggedOut />,
    document.getElementById("main")
)