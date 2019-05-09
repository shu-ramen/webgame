import React from 'react';
import { Button, Card, Container, Row, InputGroup, FormControl } from 'react-bootstrap';

export class Chat extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <Card>
                <Card.Header className="text-center" as="h5">CHAT</Card.Header>
                <Card.Body>
                    <Container>
                        <Row>
                            <p>[CPU] Hello. (2019/05/10 12:41)</p>
                        </Row>
                        <Row>
                            <p>[Player] Hi. (2019/05/10 12:42)</p>
                        </Row>
                        <Row>
                            <InputGroup className="mb-3">
                                <FormControl
                                    placeholder="write your message"
                                    aria-label="write your message"
                                    aria-describedby="basic-addon2"
                                />
                                <InputGroup.Append>
                                    <Button variant="outline-secondary">Send</Button>
                                </InputGroup.Append>
                            </InputGroup>
                        </Row>
                    </Container>
                </Card.Body>
            </Card>
        );
    }
}