var http = require('http');
var fs = require('fs');
//lets you work with files

//404 response

function send404Response(response){
    response.writeHead(404, {"Content-Type": "text/plain"});
    response.write("Error 404: page not found");
    console.log("lmaoooo");
    response.end();

}

//hande user request (listens to user request and handles the request)
function onRequest(request, response){
    if(request.method == 'GET' && request.url == '/'){
        console.log("lmaoo");
        response.writeHead(200,{"Content-Type": "text/html"});
        //sends back html
        console.log("html is sending");
        fs.createReadStream("Fourth_Project.html").pipe(response);
        console.log("wtf is happening");
    }
    else{
        send404Response(response);
    }
}
//first request = info about user's request
//response = what to send back

http.createServer(onRequest).listen(8888);
console.log("server is now running");
// parameter = what you want to run when user connects to server
