console.log("lower.js 가 로드되었습니다.");

function helloworld() {
  console.log("helloworld");
}

function display_like() {
  console.log('function display_like 실행')
  let posts = document.getElementsByClassName("sub_body_form");
  for (i = 1; i < posts.length + 1; i++) {
    // console.log(i)
    id_str = "like_" + i.toString();
    let checkbox_label = document.getElementById(id_str);
    let checkbox = checkbox_label.getElementsByTagName("input")[0];
    let checkbox_in = checkbox_label.getElementsByTagName("span")[0];


    checkbox.addEventListener("change", function (e) {
    
      // console.log(this)
      let pe = this.parentElement.parentElement
      console.log(pe)
      // let div_count = $('feed_txt')
      let div_count=pe.getElementsByClassName('feed_txt')
      console.log(div_count)
      let content = div_count.item(0)
      // console.log(div_count.innerHTML)
    
      // let content = div_count.textContent
      // let content = div_count.data()
      console.log(content)
      console.log(typeof(content))
      // console.log(content.textContent)
      content = content.textContent

      c_txt=content.substr(3,content.length)
      console.log(c_txt)

      if (checkbox.checked) {
        checkbox_in.innerHTML = `<img src="/static/images/cloud_full.png" class="like_icon" alt="" />`;

        let csrf_token = $("[name=csrfmiddlewaretoken]").val();
        let post_id = checkbox_label.getElementsByTagName("postid")[0];
        post_id = parseInt(post_id.textContent);
        $.ajax({
          type: "post",
          url: "like/",
          dataType: "json",
          data: {
            post: post_id,
            csrfmiddlewaretoken: csrf_token,
          },
          headers: { "X-CSRFToken": "{{ csrf_token }}" },
          success: function (response) {
            console.log(response);
            alert("success??!!");
          },
          error: function () {
            // console.log("error");
          },
          complete: function () {
            // console.log('complete')
          },
        });
        

      } else {
        checkbox_in.innerHTML = `<img src="/static/images/cloud_empty.png" class="like_icon" alt="" />`;

        let csrf_token = $("[name=csrfmiddlewaretoken]").val();
        let post_id = checkbox_label.getElementsByTagName("postid")[0];
        post_id = parseInt(post_id.textContent);
        $.ajax({
          type: "post",
          url: "unlike/",
          dataType: "json",
          data: {
            post: post_id,
            csrfmiddlewaretoken: csrf_token,
          },
          headers: { "X-CSRFToken": "{{ csrf_token }}" },
          success: function (response) {
            console.log(response);
            alert("success??!!");
          },
          error: function () {
            // console.log("error");
          },
          complete: function () {
            // console.log('complete')
          },
        });
      }
      // location.reload()
    });
    // checkbox_label.addEventListener("click", function () {
    //   like_count = "like_count" + i.toString();
    //   // window.location.reload()
    //   location.reload()
    //   // $("#" + like_count).load(window.location.href + "#" + like_count);
    // });
  }
}

display_like();
