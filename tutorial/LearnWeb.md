本科的时候虽然学过Web开发，但是自己始终没有利用Java从头到尾搭建一个稍微复杂些的Web系统，这里记录一下使用Java搭建一个Web程序的从头至尾的心路，也给记忆力不好的自己当做一个回忆笔记，不断记录一下这段学习的里程碑。
#概述#
##Web相关概念##
 - 胖客户端（RCP）**vs** 瘦客户端（TCP）
 - C/S **vs** B/S
##Web背景知识##
 - Web访问基本原理（浏览器输入url -> 展示网页整个过程？）
 - HTTP协议（基于TCP/IP协议的应用层协议，负责浏览器、服务器之间的交互，Web开发将这个过程封装的较为完善）
 - Web浏览器
 - Web服务器
##Web开发技术历史##
 - 传统的Web服务器模式开发， 静态页面（无法提供及时信息；修改必须重新编写HTML静态页面；不能满足多样化需求）
 - 动态展现页面技术
 	1. CGI实现动态页面生成
 		+ 每个请求生成一个操作CGI程序的进程，开销巨大；
 		+ 重复编写处理网络协议的代码；
 		+ 针对Java的CGI程序，首先启动一个进程，然后进程启动JVM，然后JVM中执行Java CGI程序，效率更加低，因此Java推出Servlet规范
 	2. Java Servlet 改进的CGI
 		- 优点
 			+ 一个操作系统进程+加载一次JVM；
 			+ 同样的处理只需加载一个类；
 			+ 可以共享处理网络协议的代码；
 			+ 与Web服务器交互，程序之间共享数据）
 		- 缺点
 			+ HTML标签和表达式嵌入Servlet程序（Java）中，修改Servlet变得复杂；
 	3. JSP：Servlet的模板
 		- 实现静态HTML和动态HTML混合编码的技术；
 		- JSP最终还是转换成Servlet，被装载入Web容器
 			+ 翻译阶段 .jsp文件转换为.java文件
 			+ 编译阶段 .java文件转换为.class文件
 			+ 请求阶段 返回生成的HTML页面
###JSP翻译原理###
 jsp源代码：
<!-- jsp -->
	<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
	<%
	String path = request.getContextPath();
	String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
	%>

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
	<html>
  		<head>
    		<base href="<%=basePath%>">
    
    		<title>My JSP 'hello.jsp' starting page</title>
    
			<meta http-equiv="pragma" content="no-cache">
			<meta http-equiv="cache-control" content="no-cache">
			<meta http-equiv="expires" content="0">    
			<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
			<meta http-equiv="description" content="This is my page">
			<!--
			<link rel="stylesheet" type="text/css" href="styles.css">
			-->

  		</head>
  
  		<body>
  			<%=new Date() %>
    		This is my JSP page. <br>
  		</body>
	</html>
翻译后的java代码（tomcat的话在 `\work\Catalina\localhost\{project_name}\org\apache\jsp`目录下寻找翻译的java文件和编译的class文件：
<!-- java -->
    package org.apache.jsp;

    import javax.servlet.*;
    import javax.servlet.http.*;
    import javax.servlet.jsp.*;
    import java.util.*;

    public final class index_jsp extends org.apache.jasper.runtime.HttpJspBase
        implements org.apache.jasper.runtime.JspSourceDependent {

      private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

      private static java.util.List _jspx_dependants;

      private javax.el.ExpressionFactory _el_expressionfactory;
      private org.apache.AnnotationProcessor _jsp_annotationprocessor;

      public Object getDependants() {
        return _jspx_dependants;
      }

      public void _jspInit() {
        _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        _jsp_annotationprocessor = (org.apache.AnnotationProcessor) getServletConfig().getServletContext().getAttribute(org.apache.AnnotationProcessor.class.getName());
      }

      public void _jspDestroy() {
      }

      public void _jspService(HttpServletRequest request, HttpServletResponse response)
            throws java.io.IOException, ServletException {

        PageContext pageContext = null;
        HttpSession session = null;
        ServletContext application = null;
        ServletConfig config = null;
        JspWriter out = null;
        Object page = this;
        JspWriter _jspx_out = null;
        PageContext _jspx_page_context = null;


        try {
          response.setContentType("text/html;charset=ISO-8859-1");
          pageContext = _jspxFactory.getPageContext(this, request, response,
          			null, true, 8192, true);
          _jspx_page_context = pageContext;
          application = pageContext.getServletContext();
          config = pageContext.getServletConfig();
          session = pageContext.getSession();
          out = pageContext.getOut();
          _jspx_out = out;

          out.write('\r');
          out.write('\n');

          String path = request.getContextPath();
          String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

          out.write("\r\n");
          out.write("\r\n");
          out.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\r\n");
          out.write("<html>\r\n");
          out.write("  <head>\r\n");
          out.write("    <base href=\"");
          out.print(basePath);
          out.write("\">\r\n");
          out.write("    \r\n");
          out.write("    <title>My JSP 'hello.jsp' starting page</title>\r\n");
          out.write("    \r\n");
          out.write("\t<meta http-equiv=\"pragma\" content=\"no-cache\">\r\n");
          out.write("\t<meta http-equiv=\"cache-control\" content=\"no-cache\">\r\n");
          out.write("\t<meta http-equiv=\"expires\" content=\"0\">    \r\n");
          out.write("\t<meta http-equiv=\"keywords\" content=\"keyword1,keyword2,keyword3\">\r\n");
          out.write("\t<meta http-equiv=\"description\" content=\"This is my page\">\r\n");
          out.write("\t<!--\r\n");
          out.write("\t<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">\r\n");
          out.write("\t-->\r\n");
          out.write("\r\n");
          out.write("  </head>\r\n");
          out.write("  \r\n");
          out.write("  <body>\r\n");
          out.write("  \t");
          out.print(new Date() );
          out.write("\r\n");
          out.write("    This is my JSP page. <br>\r\n");
          out.write("  </body>\r\n");
          out.write("</html>\r\n");
        } catch (Throwable t) {
          if (!(t instanceof SkipPageException)){
            out = _jspx_out;
            if (out != null && out.getBufferSize() != 0)
              try { out.clearBuffer(); } catch (java.io.IOException e) {}
            if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
            else log(t.getMessage(), t);
          }
        } finally {
          _jspxFactory.releasePageContext(_jspx_page_context);
        }
      }
    }
jsp只是方便了代码的书写，web服务器中最终还是将jsp->java->class的过程，生成的java文件其实就是一个Servlet程序，重要的函数为`_jspService`函数；最终该函数利用最初传统的Servlet程序的方法out出HTML标签和代码；所以JSP只是简化拼接HTML的过程，最终仍然使用的基本的技术，只是Tomcat这种Web服务器包揽了**翻译**的过程。
#准备#
##JDK环境##
- JAVA_HOME配置
- PATH添加`%JAVA_HOME%\bin`
- 讲道理JDK1.6+安装以后会自动帮你配置CLASSPATH，如果没有手动配置`.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar`
##Eclipse##
- 安装插件
- web.xml为web程序描述文件
##Tomcat##
- CATALINA_HOME配置
- PATH添加`%CATALINA_HOME\bin`
##第一个web程序##
1. Eclipse中创建Web project
2. 创建一个Servlet程序
3. web.xml中配置Servlet的信息及其子字段
4. 服务器发布（Tomcat）
<!-- xml -->
	<servlet>
	   <servlet-name></servlet-name>
	   <servlet-class></servlet-class>
	</servlet>
	<servlet-mapping>
		<servlet-name></servlet-name>
		<url-pattern></url-pattern>
	</servlet-mapping>
#Web开发具体技术#
##Servlet##
Java Web应用程序中，处理Request并且发送Response的过程由Servlet程序完成。

- HTTP协议
<br/>了解HTTP协议，Java Web开发中不太需要关注底层协议的实现，这部分Tomcat类似服务器负责；只需要编写Servlet程序，输出HTML代码。《图解HTTP协议》
- Servlet是Java Web的核心程序，所有网址请求交由Servlet程序处理
- Tomcat把request和response分别封装为HttpServletRequest和HttpServletResponse对象，根据Servlet Mapping和请求方法调用Servlet中的doPost(request, response)或doGet(request, response)等方法
- Servlet规范规定了Web程序的目录结构
<br/>Web程序文件结构 | /（Web应用根目录） | /WEB-INF/(WEB-INF文件夹，Tomcat会隐藏该文件夹下的所有文件和文件夹，保护它们不能通过浏览器直接访问) | /WEB-INF/web.xml(Web程序最主要的配置文件) | /WEB-INF/classes/(编译好的类文件存放在该目录，包括Servlet类) | /WEB-INF/lib(jar文件在该文件目录) 
- 编写Servlet直接继承HttpServlet，覆盖其常用的方法（doGet,doPost,getLastModified) -> web.xml进行配置 -> 部署
- web.xml中可以配置参数，Servlet独有的可以读取的参数配置<br/>
<!-- xml -->
	<init-param>
		<param-name></param-name>
		<param-value></param-value>
	</init-param>
取参数的方法在相应的Servlet类中利用getInitParameter或getInitParameterNames，或者利用getServletConfig获取ServletConfig对象调用同样的方法；web.xml中可以配置<br/>
<!-- xml -->
	<context-param>
		<param-name></param-name>
		<param-value></param-value>
	</context-param>
这个参数所有Servlet均可访问，获取参数方法Servlet中调用getServletConfig获取到ServletConfig对象，然后调用ServletConfig的getServletContext方法，获取到ServletContext对象，接下来使用getInitParameter或者getInitParameterNames

- 资源注射（JNDI技术）使用注解@Resource(name="")的形式；另外也可以注射数据源<br/>
<!-- xml -->
	<env-entry>
		<env-entry-name></env-entry-name>
		<env-entry-type></env-entry-type>
		<env-entry-value></env-entry-value>
	</env-entry>

- 上传表单数据
- Servlet生命周期：init(ServletConfig config)->Service(ServletRequest req, ServletResponse res)(多线程执行)->destory()；注解@PostConstruct（构造函数至init之间）和@PreDestory（destory至服务器卸载Servlet之间）
- Servlet跳转，RequestDispatcher的forward方法；重定向Redirect，返回HTTP状态吗301或302；Servlet非线程安全，谨慎使用Servlet类中变量（写入变量慎重）
##JSP##
JSP是一种简化的Servlet，最终仍然被编译为Servlet；但是其支持HTML和JAVA代码的混合，相对于Servlet中out拼接HTML代码存在优势，另外JSP不需要在web.xml进行配置可以直接部署访问；从JSP的优势来看，其更擅长于和HTML打交道，Servlet更适合和JAVA代码打交道，所以现代的JAVA EE框架，MVC分离中，Servlet专注于处理业务逻辑，JSP专注于结果显示。
###JSP历史###
Servlet不支持PHP，ASP等镶嵌HTML代码的功能，拼接HTML代码用起来过于复杂，Sun公司1999年初推出了JSP1.0，这也是JSP技术诞生的初衷，克服Servlet的拼接HTML代码、难于部署的一些缺陷
###JSP生命周期###
init->jspInit->jspService->jspDestroy->destroy，其中jspInit和jspDestroy是其相对于Servlet不同之处，复写方法如下，其中destroy不能够被复写，因为在HttpJspPage类中destroy中被声明为final类型。
<!-- html -->
	<%@ page language="java" contentType="text/html; charset=UTF-8" %>
	<%!
		public void jspInit() {
			this.log("执行 _jspInit() 方法 ... ");
		}
		public void init() {
			this.log("执行Init()方法");
		}
		public void jspDestroy() {
			this.log("执行 _jspDestory() 方法 ... ");
		}
	%>
	
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Insert title here</title>
	</head>
	<body>
	
	</body>
	</html>
###JSP简单语法###
- 模板数据
- JSP脚本 <% %>即JAVA代码
- JSP输出 <%= %>即out.println()简写
- JSP注释 <%-- --%>
- JSP变量和方法声明 <%! %>之间
- JSP中循环和条件判断比较灵活，中间可以穿插模板数据
###JSP指令###
<%@ directive {attribute=value}* %}格式，常见指令page，taglib，include等
###JSP行为###
<jsp:elements {attribute=value}* />
###JSP隐藏对象###
- out
- request
- response
- config
- session
- application
- page
- pageContext
- exception
###JSP同样可以在web.xml中进行配置，EL表达式###
##Java Bean##
关于Java Bean这个概念理解起来很困难，网上资料也异常的杂乱，但是这里推荐两篇文章，回顾了Java Bean概念的整段历史，一看就明白了Bean的这个概念。<br/><a herf="http://www.jizhuomi.com/software/585.html">Java bean的前世今生（上）</a><br/><a herf="http://www.jizhuomi.com/software/586.html">Java bean的前世今生（下）</a>
##会话跟踪##
##过滤器##
##监听器##

