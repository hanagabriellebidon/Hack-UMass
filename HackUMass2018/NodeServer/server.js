var http = require('http');
var fs = require('fs');
//lets you work with files

//404 response

function send404Response(response){
    response.writeHead(404, {"Content-Type": "text/plain"});
    response.write("Error 404: page not found");
    response.end();

}

//hande user request (listens to user request and handles the request)
function onRequest(request, response){
    if(request.method == 'GET' && request.url == '/'){
        response.writeHead(200,{"Content-Type": "text/html"});
        //sends back html
        fs.createReadStream("Fourth_Project.html").pipe(response);
    }
    else{
        send404Response(response);
    }
}
//first request = info about user's request
//response = what to send back

http.createServer(onRequest).listen(0000);
console.log("server is now running");
// parameter = what you want to run when user connects to server
