import React from 'react';
import request from 'superagent';
import { addHeader } from '../../../share/csrf.jsx';
import { Button, Card, Container, Row, InputGroup, FormControl } from 'react-bootstrap';

export class Chat extends React.Component {
    constructor() {
        super();
    }

    sendMessage() {
        let message = document.getElementById("chatMessage").value;
        document.getElementById("chatMessage").value = "";
        
        addHeader(request.post("sendchat"))
            .send({
                message: message
            })
            .end(function (err, res) {
                if (err) {
                    alert(res.text);
                }
                console.dir(res);
            }.bind(this));
    }

    render() {
        let messageTag = ""
        if (this.props.messages.length > 0) {
            messageTag = this.props.messages.slice().map((row) =>
                <Row>
                    <p>{row}</p>
                </Row>
            )
        }
        if (this.props.isStarted) {
            return (
                <Card>
                    <Card.Header className="text-center" as="h5">CHAT</Card.Header>
                    <Card.Body>
                        <Container>
                            {messageTag}
                            <Row>
                                <InputGroup className="mb-3">
                                    <FormControl
                                        placeholder="write your message"
                                        aria-label="write your message"
                                        id="chatMessage"
                                    />
                                    <InputGroup.Append>
                                        <Button variant="outline-secondary" onClick={() => this.sendMessage()}>Send</Button>
                                    </InputGroup.Append>
                                </InputGroup>
                            </Row>
                        </Container>
                    </Card.Body>
                </Card>
            );
        }
        else {
            return "";
        }
    }
}