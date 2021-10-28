import React, {Component} from 'react';
import axios from 'axios';
import Select from 'react-select';


const axios_instance = axios.create({
    baseURL: 'http://localhost:3001/',
    method: 'POST',
});


const customStyles = {
    container: base => ({
        ...base,
        flex: 1
    }),
    input: base => ({
        ...base,
        color: "white"
    }),
    control: (base, state) => ({
        ...base,
        background: "#023950",
        // match with the menu
        borderRadius: state.isFocused ? "3px 3px 0 0" : 3,
        // Overwrittes the different states of border
        //borderColor: state.isFocused ? "yellow" : "blue",
        // Removes weird border around container
        boxShadow: state.isFocused ? null : null,
            "&:hover": {
              // Overwrittes the different states of border
              //borderColor: state.isFocused ? "red" : "blue"
        },
        color: "white",
    }),
    singleValue: base => ({
        ...base,
        color: "white"
    }),
    menu: base => ({
      ...base,
      // override border radius to match the box
      borderRadius: 0,
      // kill the gap
      marginTop: 0,
      background: "#023950",
      color: "white"
      
    }),
    menuList: base => ({
      ...base,
      // kill the white space on first and last option
      padding: 0,
    })
  };


class NewGameBox extends Component {

    constructor(props) {
        super(props);

        this.state = {
            sports: [],
            games: [],
            streams: [],
            isLoadingCategory: true,
            isLoadingGame: false,
            isLoadingStream: false,
            stream_value: "",
            stream_link: ""
        };
    }

    query_data_information(asset_type, link) {
        axios_instance
        .post(
            'api/item',
            JSON.stringify({'type': asset_type, "info": {'link': link}})
        )
        .then(res => {
                if (asset_type == "game"){
                    this.setState({ streams: res.data.message });
                    this.setState({ isLoadingGame: false});
                }
                if (asset_type == "main"){ 
                    this.setState({ sports: res.data.message.categories });
                    this.setState({ games: res.data.message.games });
                    this.setState({ isLoadingCategory: false});
                }
                if (asset_type == "stream"){
                    this.setState({ stream_link: res.data.message});
                    this.setState({ isLoadingStream: false});
                }
            }
        )
    }
    
    async componentDidMount(){
        this.query_data_information('main', '/enx/allupcomingsports/1/');
    }

    menu_item_selection(link, asset_type, value) {
        if (asset_type == "main"){
            this.setState({ games: [] });
            this.setState({ streams: []});
            this.setState({ isLoadingCategory: true });
        }
        if (asset_type == "game"){
            this.setState({ stream_value: ""});
            this.setState({ streams: []});
            this.setState({ isLoadingGame: true });
        }
        if (asset_type == "stream"){
            this.setState({ stream_value: value});
            this.setState({ stream: []})
            this.setState({ isLoadingStream: true });
        }
        this.query_data_information(asset_type, link);
    }

    create_iframe(link){
        if (link){
            return (
                <table width="100%" height="100%" cellpadding="0" cellspacing="0">
                    <td bgcolor="#000d1a" align="center">
                        <iframe
                         allowFullScreen="true"
                         scrolling="no"
                         frameborder="0"
                         width="700"
                         height="480"
                         src={link[0]}>
                        </iframe>
                    </td>
                </table>
            );
        }else{
            return ;
        }
    }

    render(){
        const formatGames = ({label, date, championship}) => (
            <div>
            <h4>{label}</h4>
            <h6>{date+" "+championship}</h6>
            </div>
        );
        
        return(
            <div style={{width: "700px"}}>
                <Select
                 placeholder="Select Sport..."
                 options={this.state.sports}
                 styles={customStyles}
                 onChange={
                     opt =>
                     this.menu_item_selection(opt.link, "main", opt.value)
                    }
                 isLoading={this.state.isLoadingCategory}
                 />
                <Select
                 placeholder="Select Game..." 
                 options={this.state.games}
                 formatOptionLabel={formatGames}
                 styles={customStyles}
                 onChange={
                     opt =>
                     this.menu_item_selection(opt.link, "game", opt.value)
                    }
                 isLoading={this.state.isLoadingGame}
                 />
                <Select
                 placeholder="Languages..."
                 options={this.state.streams}
                 styles={customStyles}
                 {...(this.state.stream_value ? {} : {value: ""})}
                 onChange={
                     opt =>
                     this.menu_item_selection(opt.link, "stream", opt.value)
                    }
                 isLoading={this.state.isLoadingStream}
                 />
                <div>
                    {this.create_iframe(this.state.stream_link)}
                </div>
            </div>
        );
    }
}

export default NewGameBox;