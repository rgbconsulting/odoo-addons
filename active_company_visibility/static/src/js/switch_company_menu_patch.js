/** @odoo-module **/

import { registry } from "@web/core/registry";
import { SwitchCompanyMenu } from "@web/webclient/switch_company_menu/switch_company_menu";

export const systrayItem = {
    Component: SwitchCompanyMenu,
    isDisplayed(env) {
        return true;
    },
};

registry.category("systray").add("SwitchCompanyMenu", systrayItem, { sequence: 1 , force: true});