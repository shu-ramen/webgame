import React from 'react';
import request from 'superagent';
import { addHeader } from '../../../share/csrf.jsx';
import { Button, Card, Col, Container, Row } from 'react-bootstrap';

export class Info extends React.Component {
    constructor() {
        super();
    }

    start() {
        addHeader(request.get("./create"))
            .end(function (err, res) {
                if (err) {
                    alert(res.text);
                }
                else {
                    location.href = res.body["gameId"] + "/";
                }
            }.bind(this));
    }

    render() {
        let buttons = "";
        if (this.props.isStarted == false) {
            buttons = (
                <div>
                    <Row>
                        <Button variant="primary" size="lg" onClick={() => this.start()} block>START</Button>
                    </Row>
                </div>
            );
        }
        else {
            buttons = (
                <div>
                    <br />
                    <Row>
                        <Button variant="secondary" size="lg" block>PASS</Button>
                    </Row>
                    <br />
                    <Row>
                        <Button variant="danger" size="lg" block>GIVE UP</Button>
                    </Row>
                </div>
            )
        }

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
                        { buttons }
                    </Container>
                </Card.Body>
            </Card>
        );
    }
}