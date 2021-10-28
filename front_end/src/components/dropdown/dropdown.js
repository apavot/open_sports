import React, { useState } from 'react';
import {
    ButtonDropdown,
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem
} from 'reactstrap';


function DropDownBuild({name, data, asset_type, parent}) {
    const [dropdownOpen, setDropdownOpen] = useState(false);

    const toggle = () => setDropdownOpen(prevState => !prevState);

    function item_list(info, i) {
        return (
            <DropdownItem 
             key={name+i}
             onClick={parent.menu_item_selection.bind(parent, info.link, asset_type)}>
                <h6>{info.name}</h6>
                {asset_type == "game"
                ? <a>{info.date+" "+info.championship}</a>
                : ""
                }
            </DropdownItem>
        );
    }

    return (
        <Dropdown
         isOpen={dropdownOpen}
         toggle={toggle}
        >
            <DropdownToggle caret>
                {name} 
            </DropdownToggle>
            <DropdownMenu
             style={{
                 overflowY: 'scroll',
                 maxHeight: 300}}>
                <DropdownItem header>{name}</DropdownItem>
                {data.map((x, index) => {
                    return item_list(x, index, asset_type)})
                }                
            </DropdownMenu>
        </Dropdown>
    );
}

export default DropDownBuild;