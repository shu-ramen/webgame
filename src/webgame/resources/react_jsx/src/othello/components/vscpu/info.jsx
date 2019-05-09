import React from 'react';
import { Button, Card, Col, Container, Row } from 'react-bootstrap';

export class Info extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Card>
                <Card.Header as="h5">GAME INFO</Card.Header>
                <Card.Body>
                    <Container>
                        <Row>
                            <Col xl={8} lg={8} md={8} sm={12} xs={12}>
                                <h6>Next Player</h6>
                            </Col>
                            <Col xl={4} lg={4} md={4} sm={12} xs={12}>
                                <h6>CPU</h6>
                            </Col>
                        </Row>
                        <br />
                        <Row>
                            <Col xl={8} lg={8} md={8} sm={12} xs={12}>
                                <h6>Your Stones</h6>
                            </Col>
                            <Col xl={4} lg={4} md={4} sm={12} xs={12}>
                                <h6>2</h6>
                            </Col>
                        </Row>
                        <br />
                        <Row>
                            <Col xl={8} lg={8} md={8} sm={12} xs={12}>
                                <h6>CPU's Stones</h6>
                            </Col>
                            <Col xl={4} lg={4} md={4} sm={12} xs={12}>
                                <h6>2</h6>
                            </Col>
                        </Row>
                        <br />
                        <Row>
                            <Button variant="secondary" size="lg" block>PASS</Button>
                        </Row>
                        <br />
                        <Row>
                            <Button variant="danger" size="lg" block>GIVE UP</Button>
                        </Row>
                        <br />
                    </Container>
                </Card.Body>
            </Card>
        );
    }
}