<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
	<%@  include file="module/header.jsp" %>
	<main>
    <nav>
      <h3>글 목록</h3>
      
      <div class="nav_background">
        <ul class="nav_none_list">
        
          <li>
            <a href="">전체 글</a>
          </li>
          
          <li>
            <a href="">인기 글</a>
          </li>
          
          <li>
            <a href="">공지사항</a>
          </li>
          
          <li>
            <a href="">영화수다(자유게시판)</a>
          </li>
          
          <li>
            <a href="">일반수다(자유게시판)</a>
          </li>
          
          <li>
            <a href="">ID공유</a>
          </li>

          <li>
            <a href="">넷플릭스 정보/소식</a>
          </li>
        
        </ul>
      </div>
      
      <h3>영화목록</h3>
      <div class="nav_background">
        <ul  class="nav_none_list">
          <li style="list-style-type: none;">
            <a href="">전체영화</a>
          </li>
        
          <li style="list-style-type: none;">
            장르별
            <ul>
            
              <li>
                <a href="">스릴러</a>
              </li>
              
              <li>
                <a href="">공포</a>
              </li>
            
            </ul>
          </li>
        
          <li style="list-style-type: none;">
            출현배우
            <ul>
              <li><a href="">이병헌</a></li>
              <li><a href="">송강호</a></li>
            </ul>
          </li>
        
          <li class="nav_none_list">
            연출감독
            <ul>
              <li><a href="">봉준호</a></li>
              <li><a href="">박축욱</a></li>
            </ul>
          </li>
        
        </ul>
      </div>
    </nav>
    <section>
      <h3 id="top">TOP8</h3>
      <table border="20pt">
          <tr>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td></tr>
          <tr>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td>
              <td><img src="images/tableimgex.png" width="200pt" height="200pt"></td></tr>
      </table>
    </section>
  </main>
</body>
</html>