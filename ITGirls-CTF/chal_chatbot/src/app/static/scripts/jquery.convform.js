function SingleConvState(t){return this.input=t,this.answer="",this.next=!1,this}function ConvState(t,e,r,i,a){this.form=r,this.wrapper=t,this.current=e,this.answers={},this.parameters=i,this.originalFormHtml=a,this.scrollDown=function(){$(this.wrapper).find("#messages").stop().animate({scrollTop:$(this.wrapper).find("#messages")[0].scrollHeight},600)}.bind(this)}SingleConvState.prototype.hasNext=function(){return this.next},ConvState.prototype.destroy=function(){return!!this.originalFormHtml&&($(this.wrapper).html(this.originalFormHtml),!0)},ConvState.prototype.newState=function(t){var e=$.extend(!0,{},{name:"",noAnswer:!1,required:!0,questions:["You forgot the question!"],type:"text",multiple:!1,selected:"",answers:[]},t);return e.element=$('<input type="text" name="'+e.name+'"/>'),new SingleConvState(e)},ConvState.prototype.next=function(){if(this.current.hasNext()){if(this.current=this.current.next,this.current.input.hasOwnProperty("fork")&&this.current.input.hasOwnProperty("case")){if(this.answers.hasOwnProperty(this.current.input.fork)&&this.answers[this.current.input.fork].value!=this.current.input.case)return this.next();if(!this.answers.hasOwnProperty(this.current.input.fork))return this.next()}return!0}return!1},ConvState.prototype.printQuestion=function(){var t=this.current.input.questions,e=t[Math.floor(Math.random()*t.length)],r=e.match(/\{(.*?)\}(\:(\d)*)?/g);for(var i in r)if(r.hasOwnProperty(i)){var a=r[i].replace(/\{|\}/g,""),n=a,s=!1;if(-1!=a.indexOf(":")&&(n=n.split(":")[0],s=a.split(":")[1]),!1!==s){var p=this.answers[n].text.split(" ");e=p.length>=s?e.replace(r[i],p[s]):e.replace(r[i],this.answers[n].text)}else e=e.replace(r[i],this.answers[n].text)}var u=$(this.wrapper).find(".message.typing");setTimeout(function(){u.html(e),u.removeClass("typing").addClass("ready"),"select"==this.current.input.type&&this.printAnswers(this.current.input.answers,this.current.input.multiple),this.scrollDown(),this.current.input.hasOwnProperty("noAnswer")&&!0===this.current.input.noAnswer&&(this.next()?setTimeout(function(){var t=$('<div class="message to typing"><div class="typing_loader"></div></div>');$(this.wrapper).find("#messages").append(t),this.scrollDown(),this.printQuestion()}.bind(this),200):this.parameters.eventList.onSubmitForm(this)),$(this.wrapper).find(this.parameters.inputIdHashTagName).focus()}.bind(this),500)},ConvState.prototype.printAnswers=function(t,e){var r=!1;if(0!=this.wrapper.find("div.options").height()&&(r=!0),this.wrapper.find("div.options div.option").remove(),e){for(var i in t)if(t.hasOwnProperty(i)){var a=$('<div class="option">'+t[i].text+"</div>").data("answer",t[i]).click(function(t){Array.isArray(this.current.input.selected)||(this.current.input.selected=[]);var e=this.current.input.selected.indexOf($(t.target).data("answer").value);-1==e?(this.current.input.selected.push($(t.target).data("answer").value),$(t.target).addClass("selected")):(this.current.input.selected.splice(e,1),$(t.target).removeClass("selected")),this.wrapper.find(this.parameters.inputIdHashTagName).removeClass("error"),this.wrapper.find(this.parameters.inputIdHashTagName).val(""),this.current.input.selected.length>0?this.wrapper.find("button.submit").addClass("glow"):this.wrapper.find("button.submit").removeClass("glow")}.bind(this));this.wrapper.find("div.options").append(a),$(window).trigger("dragreset")}}else for(var i in t)if(t.hasOwnProperty(i)){a=$('<div class="option">'+t[i].text+"</div>").data("answer",t[i]).click(function(t){this.current.input.selected=$(t.target).data("answer").value,this.wrapper.find(this.parameters.inputIdHashTagName).removeClass("error"),this.wrapper.find(this.parameters.inputIdHashTagName).val(""),this.answerWith($(t.target).data("answer").text,$(t.target).data("answer")),this.wrapper.find("div.options div.option").remove()}.bind(this));this.wrapper.find("div.options").append(a),$(window).trigger("dragreset")}if(!r){var n=$(this.wrapper).find("div.options").height(),s=$(this.wrapper).find(".wrapper-messages").height();$(this.wrapper).find(".wrapper-messages").data("originalHeight",s),$(this.wrapper).find(".wrapper-messages").css({marginBottom:n,maxHeight:s-n})}"disable"==this.parameters.selectInputStyle?($(this.wrapper).find("#"+this.parameters.inputIdName).prop("disabled",!0),$(this.wrapper).find("#"+this.parameters.inputIdName).attr("placeholder",this.parameters.selectInputDisabledText)):"hide"==this.parameters.selectInputStyle&&(this.current.input.multiple?($(this.wrapper).find("#"+this.parameters.inputIdName).prop("disabled",!0),$(this.wrapper).find("#"+this.parameters.inputIdName).attr("placeholder",this.parameters.selectInputDisabledText)):($(this.wrapper).find("#"+this.parameters.inputIdName).css({display:"none"}),$(this.wrapper).find("#convForm button").css({display:"none"})))},ConvState.prototype.answerWith=function(t,e){this.current.input.hasOwnProperty("name")&&("string"==typeof e?("tel"==this.current.input.type&&(e=e.replace(/\s|\(|\)|-/g,"")),this.answers[this.current.input.name]={text:t,value:e},this.current.answer={text:t,value:e}):(this.answers[this.current.input.name]=e,this.current.answer=e),"select"!=this.current.input.type||this.current.input.multiple?$(this.current.input.element).val(e).change():$(this.current.input.element).val(e.value).change()),"password"==this.current.input.type&&(t=t.replace(/./g,"*"));var r=$('<div class="message from">'+t+"</div>");"select"==this.current.input.type&&"disable"==this.parameters.selectInputStyle?($(this.wrapper).find("#"+this.parameters.inputIdName).prop("disabled",!1),$(this.wrapper).find("#"+this.parameters.inputIdName).attr("placeholder",this.parameters.placeHolder)):"select"==this.current.input.type&&"hide"==this.parameters.selectInputStyle&&(this.current.input.multiple?($(this.wrapper).find("#"+this.parameters.inputIdName).prop("disabled",!1),$(this.wrapper).find("#"+this.parameters.inputIdName).attr("placeholder",this.parameters.placeHolder)):($(this.wrapper).find("#"+this.parameters.inputIdName).css({display:"block"}),$(this.wrapper).find("#convForm button").css({display:"block"}))),$(this.wrapper).find("div.options div.option").remove();var i=$(this.wrapper).find("div.options").height(),a=$(this.wrapper).find(".wrapper-messages").data("originalHeight");$(this.wrapper).find(".wrapper-messages").css({marginBottom:i,maxHeight:a}),$(this.wrapper).find(this.parameters.inputIdHashTagName).focus(),e.hasOwnProperty("callback")&&(this.current.input.callback=e.callback),setTimeout(function(){$(this.wrapper).find("#messages").append(r),this.scrollDown()}.bind(this),100),$(this.form).append(this.current.input.element);var n=$('<div class="message to typing"><div class="typing_loader"></div></div>');setTimeout(function(){$(this.wrapper).find("#messages").append(n),this.scrollDown()}.bind(this),150),this.parameters.eventList.onInputSubmit(this,function(){this.next()?setTimeout(function(){this.printQuestion()}.bind(this),300):this.parameters.eventList.onSubmitForm(this)}.bind(this))},function(t){t.fn.convform=function(e){var r=t(this).html();t(this).addClass("conv-form-wrapper");var i=t.extend(!0,{},{placeHolder:"Typ hier",typeInputUi:"textarea",timeOutFirstQuestion:500,buttonClassStyle:"icon2-arrow",selectInputStyle:"show",selectInputDisabledText:"Selecteer een optie",eventList:{onSubmitForm:function(t){return console.log("completed"),t.form.submit(),!0},onInputSubmit:function(t,e){t.current.input.hasOwnProperty("callback")?"string"==typeof t.current.input.callback?window[t.current.input.callback](t,e):t.current.input.callback(t,e):e()}},formIdName:"convForm",inputIdName:"userInput",loadSpinnerVisible:"",buttonText:"▶"},e),a=t(this).find("input, select, textarea").map(function(){var e={};return t(this).attr("name")&&(e.name=t(this).attr("name")),t(this).attr("data-no-answer")&&(e.noAnswer=!0),t(this).attr("required")&&(e.required=!0),t(this).attr("type")&&(e.type=t(this).attr("type")),e.questions=t(this).attr("data-conv-question").split("|"),t(this).attr("data-pattern")&&(e.pattern=t(this).attr("data-pattern")),t(this).attr("data-callback")&&(e.callback=t(this).attr("data-callback")),t(this).is("select")&&(e.type="select",e.answers=t(this).find("option").map(function(){var e={};return e.text=t(this).text(),e.value=t(this).val(),t(this).attr("data-callback")&&(e.callback=t(this).attr("data-callback")),e}).get(),t(this).prop("multiple")?(e.multiple=!0,e.selected=[]):(e.multiple=!1,e.selected="")),t(this).parent("div[data-conv-case]").length&&(e.case=t(this).parent("div[data-conv-case]").attr("data-conv-case"),e.fork=t(this).parent("div[data-conv-case]").parent("div[data-conv-fork]").attr("data-conv-fork")),e.element=this,t(this).detach(),e}).get();if(a.length){var n,s=t(this).find("form").hide();switch(i.inputIdHashTagName="#"+i.inputIdName,i.typeInputUi){case"input":n=t('<form id="'+i.formIdName+'" class="convFormDynamic"><div class="options dragscroll"></div><input id="'+i.inputIdName+'" type="text" placeholder="'+i.placeHolder+'" class="userInputDynamic"></><button type="submit" class="submit">'+i.buttonText+'</button><span class="clear"></span></form>');break;case"textarea":n=t('<form id="'+i.formIdName+'" class="convFormDynamic"><div class="options dragscroll"></div><textarea id="'+i.inputIdName+'" rows="1" placeholder="'+i.placeHolder+'" class="userInputDynamic"></textarea><button type="submit" class="submit">'+i.buttonText+'</button><span class="clear"></span></form>');break;default:return console.log("typeInputUi must be input or textarea"),!1}t(this).append('<div class="wrapper-messages"><div class="spinLoader '+i.loadSpinnerVisible+' "></div><div id="messages"></div></div>'),t(this).append(n);var p=new SingleConvState(a[0]),u=new ConvState(this,p,s,i,r);for(var o in a)0!=o&&a.hasOwnProperty(o)&&(p.next=new SingleConvState(a[o]),p=p.next);return setTimeout(function(){t.when(t("div.spinLoader").addClass("hidden")).done(function(){var e=t('<div class="message to typing"><div class="typing_loader"></div></div>');t(u.wrapper).find("#messages").append(e),u.scrollDown(),u.printQuestion()})},i.timeOutFirstQuestion),t(n).find(i.inputIdHashTagName).keypress(function(e){if(13==e.which){var r=t(this).val();if(e.preventDefault(),"select"!=u.current.input.type||u.current.input.multiple)if("select"==u.current.input.type&&u.current.input.multiple){var a;if(""!=r.trim())(a=u.current.input.answers.filter(function(t){return-1!=t.text.toLowerCase().indexOf(r.toLowerCase())})).length?-1==u.current.input.selected.indexOf(a[0].value)?(u.current.input.selected.push(a[0].value),u.wrapper.find(i.inputIdHashTagName).val("")):u.wrapper.find(i.inputIdHashTagName).val(""):u.wrapper.find(i.inputIdHashTagName).addClass("error");else u.current.input.selected.length&&t(this).parent("form").submit()}else""==r.trim()||u.wrapper.find(i.inputIdHashTagName).hasClass("error")?t(u.wrapper).find(i.inputIdHashTagName).focus():t(this).parent("form").submit();else if(u.current.input.required)u.wrapper.find("#userInputBot").addClass("error");else(a=u.current.input.answers.filter(function(t){return-1!=t.text.toLowerCase().indexOf(r.toLowerCase())})).length?(u.current.input.selected=a[0],t(this).parent("form").submit()):u.wrapper.find(i.inputIdHashTagName).addClass("error")}autosize.update(t(u.wrapper).find(i.inputIdHashTagName))}).on("input",function(e){if("select"==u.current.input.type){var r=t(this).val(),a=u.current.input.answers.filter(function(t){return-1!=t.text.toLowerCase().indexOf(r.toLowerCase())});a.length?(u.wrapper.find(i.inputIdHashTagName).removeClass("error"),u.printAnswers(a,u.current.input.multiple)):u.wrapper.find(i.inputIdHashTagName).addClass("error")}else if(u.current.input.hasOwnProperty("pattern")){new RegExp(u.current.input.pattern,"i").test(t(this).val())?u.wrapper.find(i.inputIdHashTagName).removeClass("error"):u.wrapper.find(i.inputIdHashTagName).addClass("error")}}),t(n).find("button.submit").click(function(e){var r=t(u.wrapper).find(i.inputIdHashTagName).val();if(e.preventDefault(),"select"!=u.current.input.type||u.current.input.multiple)if("select"==u.current.input.type&&u.current.input.multiple){if(u.current.input.required&&0===u.current.input.selected.length)return!1;""!=r.trim()&&r!=i.placeHolder?(a=u.current.input.answers.filter(function(t){return-1!=t.text.toLowerCase().indexOf(r.toLowerCase())})).length?-1==u.current.input.selected.indexOf(a[0].value)?(u.current.input.selected.push(a[0].value),u.wrapper.find(i.inputIdHashTagName).val("")):u.wrapper.find(i.inputIdHashTagName).val(""):u.wrapper.find(i.inputIdHashTagName).addClass("error"):u.current.input.selected.length&&(t(this).removeClass("glow"),t(this).parent("form").submit())}else""==r.trim()||u.wrapper.find(i.inputIdHashTagName).hasClass("error")?t(u.wrapper).find(i.inputIdHashTagName).focus():t(this).parent("form").submit();else{if(u.current.input.required&&!u.current.input.selected)return!1;var a;r==i.placeHolder&&(r=""),(a=u.current.input.answers.filter(function(t){return-1!=t.text.toLowerCase().indexOf(r.toLowerCase())})).length?(u.current.input.selected=a[0],t(this).parent("form").submit()):u.wrapper.find(i.inputIdHashTagName).addClass("error")}autosize.update(t(u.wrapper).find(i.inputIdHashTagName))}),t(n).submit(function(e){e.preventDefault();var r=t(this).find(i.inputIdHashTagName).val();t(this).find(i.inputIdHashTagName).val(""),"select"==u.current.input.type?u.current.input.multiple?u.answerWith(u.current.input.selected.join(", "),u.current.input.selected):u.answerWith(u.current.input.selected.text,u.current.input.selected):u.answerWith(r,r)}),"function"==typeof autosize&&($textarea=t(u.wrapper).find(i.inputIdHashTagName),autosize($textarea)),u}return!1}}(jQuery);