import { getMessage } from './modules/functionCalls.js'

(async function () {
    const message = await getMessage();

    const messageParagraph = document.querySelector('p.message');

    messageParagraph.innerHTML = message;
}());



