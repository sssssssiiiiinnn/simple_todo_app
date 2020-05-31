$(document).ready(function () {
  $(".mobile-menu__btn").click(function () {
    $("#global-container").toggleClass("menu-open");
  });
  $(".btn.cubic").click(function () {
    // $.post(URL,data,callback);
    var data = {
      title: $("#todo-title").val(),
      rank: $("#todo-rank").val(),
      deadline: $("#todo-deadline").val(),
    };
    console.log(data);
    $.ajax({
      type: "post",
      url: "/todo/register",
      data: JSON.stringify(data),
      contentType: "application/json",
      dataType: "json",
      success: function (json_data) {
        alert("success");
      },
      error: function () {
        alert("Server Error. Pleasy try again later.");
      },
    });
  });
});
