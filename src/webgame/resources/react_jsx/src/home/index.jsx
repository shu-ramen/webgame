import React from 'react'
import ReactDOM from 'react-dom'
import { Button, Card, Col, Container, Row } from 'react-bootstrap';

class Home extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Container>
                <Row>
                    <br />
                    <h1>Welcome to WebGame!</h1>
                    <br />
                </Row>
                <Row>
                    <p>There will be a lot of games in the future!!</p>
                    <br />
                </Row>
                <Row>
                    <Col>
                        <br />
                            <h4>BOARD GAMES</h4>
                        <br />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Card bg="dark" text="white" style={{ width: '18rem' }}>
                            <Card.Header>BOARD GAMES</Card.Header>
                            <Card.Body>
                                <Card.Title>OTHELLO</Card.Title>
                                <Card.Text>
                                    Simple but deep game...
                                </Card.Text>
                                <Button variant="dark" href="/othello" block>PLAY</Button>
                            </Card.Body>
                        </Card>
                        <br />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <br />
                            <h4>CARD GAMES</h4>
                        <br />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        Coming Soon!!
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <br />
                            <h4>OTHER GAMES</h4>
                        <br />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        Coming Soon!!
                    </Col>
                </Row>
            </Container>
        );
    }
}

ReactDOM.render(
    <Home />,
    document.getElementById('main')
);