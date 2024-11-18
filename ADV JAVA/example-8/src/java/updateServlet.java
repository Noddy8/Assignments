
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;

/**
 *
 * @author 15hem
 */
@WebServlet(urlPatterns = {"/updateServlet"})
public class updateServlet extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            int cid = Integer.parseInt(request.getParameter("cid"));
            int nid = Integer.parseInt(request.getParameter("nid"));
            String nname = request.getParameter("nname");
            String nphone = request.getParameter("nphone");
            String ncity = request.getParameter("ncity");
            int nage = Integer.parseInt(request.getParameter("nage"));
            try {
                Class.forName("oracle.jdbc.driver.OracleDriver");
                Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "system", "manager");
                PreparedStatement pt = con.prepareStatement("update user_details set id=?,name=?,phone=?,city=?,age=? where id=?");
                pt.setInt(1, nid);
                pt.setString(2, nname);
                pt.setString(3, nphone);
                pt.setString(4, ncity);
                pt.setInt(5, nage);
                pt.setInt(6, cid);
                pt.executeUpdate();
                response.sendRedirect("resultServlet");
            } catch (IOException | ClassNotFoundException | SQLException e) {
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
