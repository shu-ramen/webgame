import React from 'react';
import { Button, Card, Col, Container, Row } from 'react-bootstrap';

export class Info extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Card>
                <Card.Header className="text-center" as="h5">GAME INFORMTION</Card.Header>
                <Card.Body>
                    <Container>
                        <Row>
                            <Col xl={10} lg={10} md={10} sm={12} xs={12}>
                                <h6>Your Stones</h6>
                            </Col>
                            <Col xl={2} lg={2} md={2} sm={12} xs={12}>
                                <h6>{this.props.playerCount}</h6>
                            </Col>
                        </Row>
                        <br />
                        <Row>
                            <Col xl={10} lg={10} md={10} sm={12} xs={12}>
                                <h6>CPU's Stones</h6>
                            </Col>
                            <Col xl={2} lg={2} md={2} sm={12} xs={12}>
                                <h6>{this.props.cpuCount}</h6>
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
                    </Container>
                </Card.Body>
            </Card>
        );
    }
}