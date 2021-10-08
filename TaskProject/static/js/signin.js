
$(document).ready(function(){
$("#login_button",).click(function (e) {
    e.preventDefault();

  var url =$(this).attr('href_url');
  let username=$('#username').val();
  let csrf=window.CSRF_TOKEN;

  mydata={username:username,csrf:csrf};
  // console.log(mydata);
  if (username==""){
    console.log("Please enter username ")
  }
if(username){
        data = mydata;
  }

    $.ajax({
      url: url,
      type: 'POST',
      data:data,
      dataType: 'json',
      success:function(data){ 
        console.log(data);
        if(data.status==1003){
          
          window.location.href=data.url;

        }else if(data.status!=1003){
            $('#login_error').show();
            // $('#login_error').text(data.msg)
        }
        },
      
   
  });
});
});
