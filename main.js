import { getMessage } from './modules/functionCalls.js'

const message = await getMessage();

const messageParagraph = document.querySelector('p.message');

messageParagraph.innerHTML = message;


