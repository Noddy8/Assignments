
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;

/*
 *
 * @author 15hem
 */
@WebServlet(urlPatterns = {"/resultServlet"})
public class resultServlet extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<h1>Result page</h1>\n");
            out.print("<button onclick=\"document.location.href='index.html'\">Home page</button>");
            try {
                Class.forName("oracle.jdbc.driver.OracleDriver");
                Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "system", "manager");
                PreparedStatement pt = con.prepareStatement("select * from user_details");
                ResultSet rs = pt.executeQuery();
                out.print("<style>th,td{border:1px solid black;padding:2px 10px;text-align:center}</style>");
                out.print("<table style='border:2px solid black;margin-top:30px'>");
                out.print("<tr>");
                out.print("<th>Id</th><th>Name</th><th>Phone</th><th>City</th><th>Age</th>");
                out.print("</tr>");
                while (rs.next()) {
                    int id = rs.getInt(1);
                    String name = rs.getString(2);
                    String phone = rs.getString(3);
                    String city = rs.getString(4);
                    int age = rs.getInt(5);
                    out.print("<tr>");
                    out.print("<td>"+id+"</td><td>"+name+"</td><td>"+phone+"</td><td>"+city+"</td><td>"+age+"</td>");
                    out.print("<tr>");
                }
                out.print("</table>");
            } catch (Exception e) {
                out.print(e);
            }
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
