<%-- 
    Document   : 1
    Created on : Feb 22, 2024, 10:18:52 AM
    Author     : 15hem
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <% 
            int n = Integer.parseInt(request.getParameter("Number"));
            int result = 1;
            for(int a=1 ; a<=n ; a++){
                result=result*a;
            }
            out.print(result);
        %>  

    </body>
</html>

