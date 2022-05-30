$(document).ready(function () {
	$("#nav li a:not(:only-child)").click(function (e) {
		$(this).siblings(".nav-dropdown").toggle();
		// Close one dropdown when selecting another
		$(".nav-dropdown").not($(this).siblings()).hide();
		e.stopPropagation();
	});
	$("#search-icon").click(function () {
		$(this).toggleClass("fa-times");
		$("#search-box").toggleClass("active");
	});
	// Clicking away from dropdown will remove the dropdown class
	$("html").click(function () {
		$(".nav-dropdown").hide();
	});

	$("#menu").click(function () {
		$(this).toggleClass("fa-times");
		$(".navbar").toggleClass("nav-toggle");
	});

	$(window).on("scroll load", function () {
		$("#search-icon").removeClass("fa-times");
		$("#search-box").removeClass("active");
		$("#menu").removeClass("fa-times");
		$(".navbar").removeClass("nav-toggle");
	});
});

function copy(url) {
	/* Copy the text inside the text field */
	navigator.clipboard.writeText(url).then(function () {
		alert("Copied the text: " + url);
}
	)

	
}

