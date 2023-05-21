// Copyright (c) 2023, ZeltenLabs and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hotel Room", {
	refresh(frm) {
        // Fetch the occupancy data from the server.
        frappe.call({
            method: 'hospitality.hotel.doctype.hotel_room.hotel_room.get_occupancy_data',
            args: {
                room_name: frm.doc.name
            },
            callback: function(response) {
                var dataPoints = response.message;

                var occupancyData = {
                    dataPoints: dataPoints,
                    start: new Date(), // Today
                    end: new Date(new Date().setFullYear(new Date().getFullYear() + 1)), // Today + 1 year
                };
                // console.log("occupancy data::::",occupancyData, frm.doc.name);

                // Create the chart.
                var chart = new frappe.Chart('#occupancy_chart-container', {
                    title: 'Room Occupancy',
                    data: occupancyData,
                    type: 'heatmap',
                });
                
                chart.render();
            }
        });
	},
});
