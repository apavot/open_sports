(this.webpackJsonplive_sports=this.webpackJsonplive_sports||[]).push([[0],{31:function(e,t,a){},32:function(e,t,a){},71:function(e,t,a){"use strict";a.r(t);var n=a(0),s=a.n(n),i=a(4),r=a.n(i),o=(a(31),a.p,a(32),a(9)),c=a.n(o),u=a(20),l=a(21),d=a(22),h=a(26),m=a(25),g=a(2),j=a(23),b=a.n(j),p=a(5),f=a(1),O=b.a.create({baseURL:"http://localhost:3001/",method:"POST"}),v={container:function(e){return Object(g.a)(Object(g.a)({},e),{},{flex:1})},input:function(e){return Object(g.a)(Object(g.a)({},e),{},{color:"white"})},control:function(e,t){return Object(g.a)(Object(g.a)({},e),{},{background:"#023950",borderRadius:t.isFocused?"3px 3px 0 0":3,boxShadow:(t.isFocused,null),"&:hover":{},color:"white"})},singleValue:function(e){return Object(g.a)(Object(g.a)({},e),{},{color:"white"})},menu:function(e){return Object(g.a)(Object(g.a)({},e),{},{borderRadius:0,marginTop:0,background:"#023950",color:"white"})},menuList:function(e){return Object(g.a)(Object(g.a)({},e),{},{padding:0})}},S=function(e){Object(h.a)(a,e);var t=Object(m.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).state={sports:[],games:[],streams:[],isLoadingCategory:!0,isLoadingGame:!1,isLoadingStream:!1,stream_value:"",stream_link:""},n}return Object(d.a)(a,[{key:"query_data_information",value:function(e,t){var a=this;O.post("api/item",JSON.stringify({type:e,info:{link:t}})).then((function(t){"game"==e&&(a.setState({streams:t.data.message}),a.setState({isLoadingGame:!1})),"main"==e&&(a.setState({sports:t.data.message.categories}),a.setState({games:t.data.message.games}),a.setState({isLoadingCategory:!1})),"stream"==e&&(a.setState({stream_link:t.data.message}),a.setState({isLoadingStream:!1}))}))}},{key:"componentDidMount",value:function(){var e=Object(u.a)(c.a.mark((function e(){return c.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this.query_data_information("main","/enx/allupcomingsports/1/");case 1:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"menu_item_selection",value:function(e,t,a){"main"==t&&(this.setState({games:[]}),this.setState({streams:[]}),this.setState({isLoadingCategory:!0})),"game"==t&&(this.setState({stream_value:""}),this.setState({streams:[]}),this.setState({isLoadingGame:!0})),"stream"==t&&(this.setState({stream_value:a}),this.setState({stream:[]}),this.setState({isLoadingStream:!0})),this.query_data_information(t,e)}},{key:"create_iframe",value:function(e){return e?Object(f.jsx)("table",{width:"100%",height:"100%",cellpadding:"0",cellspacing:"0",children:Object(f.jsx)("td",{bgcolor:"#000d1a",align:"center",children:Object(f.jsx)("iframe",{allowFullScreen:"true",scrolling:"no",frameborder:"0",width:"700",height:"480",src:e[0]})})}):void 0}},{key:"render",value:function(){var e=this;return Object(f.jsxs)("div",{style:{width:"700px"},children:[Object(f.jsx)(p.a,{placeholder:"Select Sport...",options:this.state.sports,styles:v,onChange:function(t){return e.menu_item_selection(t.link,"main",t.value)},isLoading:this.state.isLoadingCategory}),Object(f.jsx)(p.a,{placeholder:"Select Game...",options:this.state.games,formatOptionLabel:function(e){var t=e.label,a=e.date,n=e.championship;return Object(f.jsxs)("div",{children:[Object(f.jsx)("h4",{children:t}),Object(f.jsx)("h6",{children:a+" "+n})]})},styles:v,onChange:function(t){return e.menu_item_selection(t.link,"game",t.value)},isLoading:this.state.isLoadingGame}),Object(f.jsx)(p.a,Object(g.a)(Object(g.a)({placeholder:"Languages...",options:this.state.streams,styles:v},this.state.stream_value?{}:{value:""}),{},{onChange:function(t){return e.menu_item_selection(t.link,"stream",t.value)},isLoading:this.state.isLoadingStream})),Object(f.jsx)("div",{children:this.create_iframe(this.state.stream_link)})]})}}]),a}(n.Component),_=S;var x=function(){return Object(f.jsx)("div",{className:"App",children:Object(f.jsx)("header",{className:"App-header",children:Object(f.jsx)(_,{})})})},L=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,73)).then((function(t){var a=t.getCLS,n=t.getFID,s=t.getFCP,i=t.getLCP,r=t.getTTFB;a(e),n(e),s(e),i(e),r(e)}))};a(70);r.a.render(Object(f.jsx)(s.a.StrictMode,{children:Object(f.jsx)(x,{})}),document.getElementById("root")),L()}},[[71,1,2]]]);
//# sourceMappingURL=main.65e19a49.chunk.js.map