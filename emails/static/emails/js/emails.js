function sendForm()
{
    console.log("Mandando form");
    let data = {"email": $("#email").val(),
                "mensaje": $("#mensaje").val()}
    data = JSON.stringify(data);
    let callbackFunctionSuc = sendSuc;
    let callbackFunctionFail = sendFail;
    //url, data, callbackFunctionSuc, callbackFunctionFail
    fetchRequest.makePostRequest(
        wsSendEmail,
        data,
        callbackFunctionSuc,
        callbackFunctionFail
    );
}


function sendSuc(data)
{
    if(data.success == "true")
    {
        console.log(data);
    }
    else
    {
        sendFail();
    }
}

function sendFail(data)
{
    console.log("Falla");
}
