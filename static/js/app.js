$(document).ready(function () {
  $.ajax({
    method: "GET",
    url: "https://benjaminportfolio-v1.herokuapp.com/api/",
    dataType: "json",
  }).done(function (data) {
    console.log(data);
    $.each(data, function (i, project) {
      $("div#project").append(
        `<div class="col-md-4 col-sm-12 project-image pb-4">
        <h4>${project.title}</h4>
        <div id=${project.id}img>
          
          <img class="img-fluid" src="${project.image}" alt="" />
        </div>
          <div id=${project.id}des class="description">
            <div class="card">
              <div class="card-body">
              ${project.description}
              </div>
              <a href=${project.link} target="_blank" class="btn btn-dark" >Visit site</a>
            </div>
          </div>
        </div>
        `
      );
      $(`#${project.id}img`).click(function () {
        $(`#${project.id}des`).show(400);
        $(`#${project.id}img`).hide(400);
      });
      $(`#${project.id}des`).click(function () {
        $(`#${project.id}img`).show(400);
        $(`#${project.id}des`).hide(400);
      });
    });
  });
});
