import React from 'react';
import ReactDOM from 'react-dom';
import { Navbar, Nav, NavDropdown, Form, Button, ButtonToolbar, ButtonGroup } from 'react-bootstrap';

class Header extends React.Component {
    constructor() {
        super();
    }

    getNavbarContent(authenticated) {
        if (authenticated) {
            return (
                <Nav className="mr-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <NavDropdown title="Games" id="basic-nav-dropdown">
                        <NavDropdown.Item href="/othello">Othello</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            );
        }
        else {
            return (
                <Nav className="mr-auto">
                </Nav>
            );
        }
    }

    getNavbarForm(authenticated) {
        if (authenticated) {
            return (
                <Form inline>
                    <ButtonToolbar>
                        <ButtonGroup>
                            <Button variant="outline-secondary" href="#">Account Settings</Button>
                            <Button variant="outline-danger" href="/accounts/logout/">Log Out</Button>
                        </ButtonGroup>
                    </ButtonToolbar>
                </Form>
            );
        }
        else {
            return (
                <Form inline>
                    <ButtonToolbar>
                        <ButtonGroup>
                            <Button variant="outline-primary" href="/accounts/login/">Log In</Button>
                            <Button variant="outline-success" href="/accounts/signup/">Sign Up</Button>
                        </ButtonGroup>
                    </ButtonToolbar>
                </Form>
            );
        }
    }
    
    render() {
        let navbarContent = this.getNavbarContent(this.props.authenticated);
        let navbarForm = this.getNavbarForm(this.props.authenticated);

        return (
            <Navbar bg="light" expand="lg">
                <Navbar.Brand href="/">WebGame</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    {navbarContent}
                    {navbarForm}
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

if (document.getElementById('not-authenticated-header') != null) {
    ReactDOM.render(
        <Header authenticated={false} />,
        document.getElementById('not-authenticated-header')
    );
}

if (document.getElementById('authenticated-header') != null) {
    ReactDOM.render(
        <Header authenticated={true} />,
        document.getElementById('authenticated-header')
    );
}