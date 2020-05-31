$(document).ready(function () {
  $(".mobile-menu__btn").click(function () {
    $("#global-container").toggleClass("menu-open");
  });
  $(".btn.register").click(function () {
    // $.post(URL,data,callback);
    var data = {
      title: $("#todo-title").val(),
      rank: $("#todo-rank").val(),
      deadline: $("#todo-deadline").val(),
    };
    $("#todo-title").val("");
    $("#todo-rank").val("");
    $("#todo-deadline").val("");
    console.log(data);
    $.ajax({
      type: "post",
      url: "/todo/register",
      data: JSON.stringify(data),
      contentType: "application/json",
      dataType: "json",
      success: function (json_data) {
        alert("success");
        reload_table();
      },
      error: function () {
        alert("Server Error. Pleasy try again later.");
      },
    });
  });
  $(".btn.send").click(function () {
    console.log("send mail");
    $.ajax({
      type: "get",
      url: "/todo/send-mail",
      dataType: "json",
      success: function (json_data) {
        alert("success");
      },
      error: function () {
        alert("Server Error. Pleasy try again later.");
      },
    });
  });

  reload_table();
});

function initialize_table() {
  $.when(reload_table()).done(function () {
    console.log("done");
    $(".btn.delete").click(function () {
      var data = { id: $(this).attr("id") };
      console.log(data);
      $.ajax({
        type: "post",
        url: "/todo/delete",
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
    console.log("done");
  });
}

function reload_table() {
  $.ajax({
    type: "get",
    url: "/todo/get",
    dataType: "json",
    success: function (data) {
      dataArray = data.data;
      clearTable();
      $.each(dataArray, function (i, data) {
        var td_id = $("<td></td>");
        td_id.append(data.id);

        var td_createDate = $("<td></td>");
        td_createDate.append(data.create_date);

        var td_title = $("<td></td>");
        td_title.append(data.title);

        var td_deadline = $("<td></td>");
        td_deadline.append(data.deadline);

        var td_rank = $("<td></td>");
        td_rank.append(data.rank);

        var tr = $("<tr />");
        tr.append(td_id);
        tr.append(td_createDate);
        tr.append(td_title);
        tr.append(td_rank);
        tr.append(td_deadline);
        tr.append(
          `<td><button class="btn slide-bg delete" id="${data.id}">Delete</button></td>`
        );
        $("#todo-table-body").append(tr);
      });
      $(".btn.delete").off();
      $(".btn.delete").click(function () {
        var data = { id: $(this).attr("id") };
        $.ajax({
          type: "post",
          url: "/todo/delete",
          data: JSON.stringify(data),
          contentType: "application/json",
          dataType: "json",
          success: function (json_data) {
            alert("success");
            reload_table();
          },
          error: function () {
            alert("Server Error. Pleasy try again later.");
          },
        });
      });
    },
    error: function () {
      alert("Server Error. Pleasy try again later.");
    },
  });
}

function clearTable() {
  $("#todo-table-body > tr").remove();
}
