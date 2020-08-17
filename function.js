function getOperationType(){
    var operation = document.getElementById('options');
    var operationStr = operation.options[operation.selectedIndex].value;
    getHTTPRequest(operationStr);
}

function instructionsDisplay(){
    var state = document.getElementById('options');
    var DDState = state.options[state.selectedIndex].value;
    var instructions = document.getElementById('Instructions');
    if(DDState == "Read"){
        instructions.innerHTML = "Please Enter the Ticker Symbol you would Like to search for.";
    }
    else if(DDState == "Create"){
        instructions.innerHTML = 'Please enter the new Ticker in JSON format EXAMPLE {"Ticker":"EXAMPLE"}'
    }
    else if(DDState == "Update"){
        instructions.innerHTML = 'Please enter the new Ticker values in JSON format then the ticker symbol you wish to update in plaintext EXAMPLE {"Ticker":"NEWVAL"} OLDVAL'
    }
    else if(DDState == "Delete"){
        instructions.innerHTML = 'Please enter the Ticker Symbol to be deleted EXAMPLE AA'
    }
}

function getHTTPRequest(operation){
    var JSON = document.getElementById('JSON').value;
    console.log(JSON);
    if(operation == "Read"){
         var url = 'http://localhost:8080/stocks/api/v1.0/getStock/' + JSON;
        console.log(url);
        UserAction(url, "GET", JSON);
    }
    else if(operation == "Delete"){
        var url = 'http://localhost:8080/stocks/api/v1.0/deleteStock/' + JSON;
        console.log(url);
        UserAction(url, "GET" , JSON)
    }
    else if(operation == "Create"){
        var url = 'http://localhost:8080/stocks/api/v1.0/createStock/blah';
        console.log(url);
        UserAction(url, "POST", JSON);
    }
    else if(operation == "Update"){
        var endOfJson = false;
        var stockUpdate = JSON.split("}");
        stockUpdate[0] = stockUpdate[0] + "}";
        stockUpdate[1] = stockUpdate[1].trim();
        var url = 'http://localhost:8080/stocks/api/v1.0/updateStock/' + stockUpdate[1];
        console.log(url);
        UserAction(url, "POST" , stockUpdate[0]);
    }
}

function UserAction(url, requestType, JSON){
    var xhttp = new XMLHttpRequest({mozSystem: true});
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            var response = xhttp.response;
            var results = document.getElementById('JSONResults');
            results.innerHTML = response;
            console.log("ok " + response);
        }
    };
    if(requestType == "GET"){
        xhttp.open(requestType , url, true);
        xhttp.send();
    }
    else{ 
        xhttp.open(requestType, url, true);
        xhttp.setRequestHeader('Content-Type', 'application/json' );
        xhttp.send(JSON);
    }
}
