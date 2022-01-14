$(document).ready(function() {
	$("tbody tr").hover(function() {
		$(this).find("td").addClass("hov");
	}, function() {
		$(this).find("td").removeClass("hov");
	});

	//페이지 단위 작업
	var rows = $("table").find("tbody tr").length;   //<tr>의 전체 수
	//alert(rows);
	var per_page = 5;
	var no_pages = Math.ceil(rows / per_page);    //페이지 수 얻기.
	//alert(no_pages);
	var pageNumbers = $("<div id='pages'></div>");
	for(var i = 0; i <no_pages; i++) {
		$("<span class='page'>"+(i+1) +"</span>").appendTo(pageNumbers);  //pageNumbers앞에 <span>태그를 밀어 넣었다.
	}
	pageNumbers.insertBefore("table"); //table 태그 앞에 pageNumbers안에 있는 내용이 들어간다.

	//페이지 링크 걸기
	$(".page").hover(function() {  //<span class='page'>"+(i+1) +"</span> 이녀석을 지칭함.
		$(this).addClass("hov");
	}, function() {
		$(this).removeClass("hov");
	});

	$("table").find("tbody tr").hide();    //.find = table안에 있는 무엇을 찾는다.
	var t = $("table tbody tr");   //배열이다. 모든 tr이 튀어나온다. 13개.
	for ( var j = 0; j <= per_page-1 ; j++) {  //먼저 5개 출력
		$(t[j]).show();
	}

	$("span").click(function(event) {
		$("table").find("tbody tr").hide();
		//for ( var k = 1-1 * 5; k < (1 * 5 - 1) ; k++)   0~4까지돈다.
		//for ( var k = 2-1 * 5; k < (2 * 5 - 1) ; k++)   5~9까지 돈다.
		//for ( var k = 3-1 * 5; k < (3 * 5 - 1) ; k++)   10~14까지 돈다.
		for ( var k = ($(this).text() -1 ) * per_page; k <= $(this).text() * per_page -1 ; k++) {  //$(this).text() = span태그의 값부터~~ 즉 , 1찍으면 1, 2찍으면 2, 3찍으면 3부터,,,
			$(t[k]).show();
		}
	});
});