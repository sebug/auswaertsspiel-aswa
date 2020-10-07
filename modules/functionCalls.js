async function getMessage() {
    const messageResult = await fetch('/api/GetMessage?name=SampleUser');
    const resultJson = await messageResult.text();
    return resultJson;
}

export { getMessage };
