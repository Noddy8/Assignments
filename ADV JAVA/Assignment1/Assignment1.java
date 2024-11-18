package assignment1;

import java.sql.*;

public class Assignment1 {

    public static void main(String[] args) throws ClassNotFoundException {
        try {
            Class.forName("oracle.jdbc.driver.OracleDriver");
            String url = "jdbc:oracle:thin:@localhost:1521:XE";
            Connection con = DriverManager.getConnection(url, "system", "manager");
            Statement st = con.createStatement();
            // String s = "create table student(id number(10),name varchar2(20),age number(10))";
            //st.executeQuery(s);
            //String ins = "insert into student values(103 ,'Jay',20)";
            //st.executeUpdate(ins);
            //String upd = "update student set age=21 where id=102";
            //st.executeUpdate(upd);
            String d = "delete FROM STUDENT where name='Jeet'";
            st.executeUpdate(d);
            //String text = "select * from student";
            //ResultSet rs = st.executeQuery(text);
            //int count = 1;
            //while (rs.next()) {
               // int id = rs.getInt(1);
               // String name = rs.getString(2);
               // int age = rs.getInt(3);
               // System.out.println("-> Student - "+count);
               //System.out.println("  id   : "+id+"\n  Name : "+name+"\n  Age  : "+age+"\n");
               // count++;
        } catch (Exception e) {
            System.out.println(e);
        }
    }

}
