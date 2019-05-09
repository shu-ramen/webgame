import React from 'react';
import ReactDOM from 'react-dom';
import { Button, Card, Col, Container, Row } from 'react-bootstrap';

class Index extends React.Component {
    constructor() {
        super();
    }
    
    render() {
        return (
            <div>
                <Container>
                    <Row>
                        <Col>
                            <br />
                            <h4>VS CPU MODE</h4>
                            <br />
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Card bg="dark" text="white" style={{ width: '18rem' }}>
                                <Card.Header>CPU</Card.Header>
                                <Card.Body>
                                    <Card.Title>LEVEL 1</Card.Title>
                                    <Card.Text>
                                        Let's battle with CPU (LEVEL 1)
                                    </Card.Text>
                                    <Button variant="dark" block>START</Button>
                                </Card.Body>
                            </Card>
                            <br />
                        </Col>
                        <Col>
                            <Card bg="dark" text="white" style={{ width: '18rem' }}>
                                <Card.Header>CPU</Card.Header>
                                <Card.Body>
                                    <Card.Title>LEVEL 2</Card.Title>
                                    <Card.Text>
                                        Let's battle with CPU (LEVEL 2)
                                    </Card.Text>
                                    <Button variant="dark" block>START</Button>
                                </Card.Body>
                            </Card>
                            <br />
                        </Col>
                        <Col>
                            <Card bg="dark" text="white" style={{ width: '18rem' }}>
                                <Card.Header>CPU</Card.Header>
                                <Card.Body>
                                    <Card.Title>LEVEL 3</Card.Title>
                                    <Card.Text>
                                        Let's battle with CPU (LEVEL 3)
                                    </Card.Text>
                                    <Button variant="dark" block>START</Button>
                                </Card.Body>
                            </Card>
                            <br />
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <br />
                            <h4>ONLINE MATCHING MODE</h4>
                            <br />
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Card bg="success" text="white" style={{ width: '18rem' }}>
                                <Card.Header>Othello Matching</Card.Header>
                                <Card.Body>
                                    <Card.Title>CREATE</Card.Title>
                                    <Card.Text>
                                        Let's create new battle with somebody online.
                                    </Card.Text>
                                    <Button variant="success" block>START</Button>
                                </Card.Body>
                            </Card>
                            <br />
                        </Col>
                        <Col>
                            <Card bg="info" text="white" style={{ width: '18rem' }}>
                                <Card.Header>Othello Matching</Card.Header>
                                <Card.Body>
                                    <Card.Title>JOIN</Card.Title>
                                    <Card.Text>
                                        Let's join to the battle with somebody online.
                                    </Card.Text>
                                    <Button variant="info" block>START</Button>
                                </Card.Body>
                            </Card>
                            <br />
                        </Col>
                        <Col>
                            <Card bg="light" text="black" style={{ width: '18rem' }}>
                                <Card.Header>Othello Matching</Card.Header>
                                <Card.Body>
                                    <Card.Title>WATCH</Card.Title>
                                    <Card.Text>
                                        Let's watch the battle with somebody online.
                                    </Card.Text>
                                    <Button variant="light" block>START</Button>
                                </Card.Body>
                            </Card>
                            <br />
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

ReactDOM.render(
    <Index />,
    document.getElementById('main')
);