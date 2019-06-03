from plotly.basewidget import BaseFigureWidget
from plotly.graph_objs import (
    Area, Bar, Barpolar, Box, Candlestick, Carpet, Choropleth, Cone, Contour,
    Contourcarpet, Funnel, Funnelarea, Heatmap, Heatmapgl, Histogram,
    Histogram2d, Histogram2dContour, Isosurface, Mesh3d, Ohlc, Parcats,
    Parcoords, Pie, Pointcloud, Sankey, Scatter, Scatter3d, Scattercarpet,
    Scattergeo, Scattergl, Scattermapbox, Scatterpolar, Scatterpolargl,
    Scatterternary, Splom, Streamtube, Sunburst, Surface, Table, Violin,
    Volume, Waterfall
)


class FigureWidget(BaseFigureWidget):

    def __init__(
        self,
        data=None,
        layout=None,
        frames=None,
        skip_invalid=False,
        **kwargs
    ):
        """
        Create a new FigureWidget instance
        
        Parameters
        ----------
        data
            The 'data' property is a tuple of trace instances
            that may be specified as:
              - A list or tuple of trace instances
                (e.g. [Scatter(...), Bar(...)])
              - A list or tuple of dicts of string/value properties where:
                - The 'type' property specifies the trace type
                    One of: ['area', 'bar', 'barpolar', 'box',
                             'candlestick', 'carpet', 'choropleth', 'cone',
                             'contour', 'contourcarpet', 'funnel',
                             'funnelarea', 'heatmap', 'heatmapgl',
                             'histogram', 'histogram2d',
                             'histogram2dcontour', 'isosurface', 'mesh3d',
                             'ohlc', 'parcats', 'parcoords', 'pie',
                             'pointcloud', 'sankey', 'scatter',
                             'scatter3d', 'scattercarpet', 'scattergeo',
                             'scattergl', 'scattermapbox', 'scatterpolar',
                             'scatterpolargl', 'scatterternary', 'splom',
                             'streamtube', 'sunburst', 'surface', 'table',
                             'violin', 'volume', 'waterfall']
        
                - All remaining properties are passed to the constructor of
                  the specified trace type
        
                (e.g. [{'type': 'scatter', ...}, {'type': 'bar, ...}])
            
        layout
            The 'layout' property is an instance of Layout
            that may be specified as:
              - An instance of plotly.graph_objs.Layout
              - A dict of string/value properties that will be passed
                to the Layout constructor
        
                Supported dict properties:
                    
                    angularaxis
                        plotly.graph_objs.layout.AngularAxis instance
                        or dict with compatible properties
                    annotations
                        plotly.graph_objs.layout.Annotation instance or
                        dict with compatible properties
                    annotationdefaults
                        When used in a template (as
                        layout.template.layout.annotationdefaults),
                        sets the default property values to use for
                        elements of layout.annotations
                    autosize
                        Determines whether or not a layout width or
                        height that has been left undefined by the user
                        is initialized on each relayout. Note that,
                        regardless of this attribute, an undefined
                        layout width or height is always initialized on
                        the first call to plot.
                    bargap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    bargroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    barmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "stack", the bars are stacked on top of one
                        another With "relative", the bars are stacked
                        on top of one another, with negative values
                        below the axis, positive values above With
                        "group", the bars are plotted next to one
                        another centered around the shared location.
                        With "overlay", the bars are plotted over one
                        another, you might need to an "opacity" to see
                        multiple bars.
                    barnorm
                        Sets the normalization for bar traces on the
                        graph. With "fraction", the value of each bar
                        is divided by the sum of all values at that
                        location coordinate. "percent" is the same but
                        multiplied by 100 to show percentages.
                    boxgap
                        Sets the gap (in plot fraction) between boxes
                        of adjacent location coordinates. Has no effect
                        on traces that have "width" set.
                    boxgroupgap
                        Sets the gap (in plot fraction) between boxes
                        of the same location coordinate. Has no effect
                        on traces that have "width" set.
                    boxmode
                        Determines how boxes at the same location
                        coordinate are displayed on the graph. If
                        "group", the boxes are plotted next to one
                        another centered around the shared location. If
                        "overlay", the boxes are plotted over one
                        another, you might need to set "opacity" to see
                        them multiple boxes. Has no effect on traces
                        that have "width" set.
                    calendar
                        Sets the default calendar system to use for
                        interpreting and displaying dates throughout
                        the plot.
                    clickmode
                        Determines the mode of single click
                        interactions. "event" is the default value and
                        emits the `plotly_click` event. In addition
                        this mode emits the `plotly_selected` event in
                        drag modes "lasso" and "select", but with no
                        event data attached (kept for compatibility
                        reasons). The "select" flag enables selecting
                        single data points via click. This mode also
                        supports persistent selections, meaning that
                        pressing Shift while clicking, adds to /
                        subtracts from an existing selection. "select"
                        with `hovermode`: "x" can be confusing,
                        consider explicitly setting `hovermode`:
                        "closest" when using this feature. Selection
                        events are sent accordingly as long as "event"
                        flag is set as well. When the "event" flag is
                        missing, `plotly_click` and `plotly_selected`
                        events are not fired.
                    coloraxis
                        plotly.graph_objs.layout.Coloraxis instance or
                        dict with compatible properties
                    colorscale
                        plotly.graph_objs.layout.Colorscale instance or
                        dict with compatible properties
                    colorway
                        Sets the default trace colors.
                    datarevision
                        If provided, a changed value tells
                        `Plotly.react` that one or more data arrays has
                        changed. This way you can modify arrays in-
                        place rather than making a complete new copy
                        for an incremental change. If NOT provided,
                        `Plotly.react` assumes that data arrays are
                        being treated as immutable, thus any data array
                        with a different identity from its predecessor
                        contains new data.
                    direction
                        Legacy polar charts are deprecated! Please
                        switch to "polar" subplots. Sets the direction
                        corresponding to positive angles in legacy
                        polar charts.
                    dragmode
                        Determines the mode of drag interactions.
                        "select" and "lasso" apply only to scatter
                        traces with markers or text. "orbit" and
                        "turntable" apply only to 3D scenes.
                    editrevision
                        Controls persistence of user-driven changes in
                        `editable: true` configuration, other than
                        trace names and axis titles. Defaults to
                        `layout.uirevision`.
                    extendfunnelareacolors
                        If `true`, the funnelarea slice colors (whether
                        given by `funnelareacolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendpiecolors
                        If `true`, the pie slice colors (whether given
                        by `piecolorway` or inherited from `colorway`)
                        will be extended to three times its original
                        length by first repeating every color 20%
                        lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendsunburstcolors
                        If `true`, the sunburst slice colors (whether
                        given by `sunburstcolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    font
                        Sets the global font. Note that fonts used in
                        traces and other layout components inherit from
                        the global font.
                    funnelareacolorway
                        Sets the default funnelarea slice colors.
                        Defaults to the main `colorway` used for trace
                        colors. If you specify a new list here it can
                        still be extended with lighter and darker
                        colors, see `extendfunnelareacolors`.
                    funnelgap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    funnelgroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    funnelmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "stack", the bars are stacked on top of one
                        another With "group", the bars are plotted next
                        to one another centered around the shared
                        location. With "overlay", the bars are plotted
                        over one another, you might need to an
                        "opacity" to see multiple bars.
                    geo
                        plotly.graph_objs.layout.Geo instance or dict
                        with compatible properties
                    grid
                        plotly.graph_objs.layout.Grid instance or dict
                        with compatible properties
                    height
                        Sets the plot's height (in px).
                    hiddenlabels
                        hiddenlabels is the funnelarea & pie chart
                        analog of visible:'legendonly' but it can
                        contain many labels, and can simultaneously
                        hide slices from several pies/funnelarea charts
                    hiddenlabelssrc
                        Sets the source reference on plot.ly for
                        hiddenlabels .
                    hidesources
                        Determines whether or not a text link citing
                        the data source is placed at the bottom-right
                        cored of the figure. Has only an effect only on
                        graphs that have been generated via forked
                        graphs from the plotly service (at
                        https://plot.ly or on-premise).
                    hoverdistance
                        Sets the default distance (in pixels) to look
                        for data to add hover labels (-1 means no
                        cutoff, 0 means no looking for data). This is
                        only a real distance for hovering on point-like
                        objects, like scatter points. For area-like
                        objects (bars, scatter fills, etc) hovering is
                        on inside the area and off outside, but these
                        objects will not supersede hover on point-like
                        objects in case of conflict.
                    hoverlabel
                        plotly.graph_objs.layout.Hoverlabel instance or
                        dict with compatible properties
                    hovermode
                        Determines the mode of hover interactions. If
                        `clickmode` includes the "select" flag,
                        `hovermode` defaults to "closest". If
                        `clickmode` lacks the "select" flag, it
                        defaults to "x" or "y" (depending on the
                        trace's `orientation` value) for plots based on
                        cartesian coordinates. For anything else the
                        default value is "closest".
                    images
                        plotly.graph_objs.layout.Image instance or dict
                        with compatible properties
                    imagedefaults
                        When used in a template (as
                        layout.template.layout.imagedefaults), sets the
                        default property values to use for elements of
                        layout.images
                    legend
                        plotly.graph_objs.layout.Legend instance or
                        dict with compatible properties
                    mapbox
                        plotly.graph_objs.layout.Mapbox instance or
                        dict with compatible properties
                    margin
                        plotly.graph_objs.layout.Margin instance or
                        dict with compatible properties
                    meta
                        Assigns extra meta information that can be used
                        in various `text` attributes. Attributes such
                        as the graph, axis and colorbar `title.text`,
                        annotation `text` `trace.name` in legend items,
                        `rangeselector`, `updatemenues` and `sliders`
                        `label` text all support `meta`. One can access
                        `meta` fields using template strings:
                        `%{meta[i]}` where `i` is the index of the
                        `meta` item in question. `meta` can also be an
                        object for example `{key: value}` which can be
                        accessed %{meta[key]}.
                    metasrc
                        Sets the source reference on plot.ly for  meta
                        .
                    modebar
                        plotly.graph_objs.layout.Modebar instance or
                        dict with compatible properties
                    orientation
                        Legacy polar charts are deprecated! Please
                        switch to "polar" subplots. Rotates the entire
                        polar by the given angle in legacy polar
                        charts.
                    paper_bgcolor
                        Sets the color of paper where the graph is
                        drawn.
                    piecolorway
                        Sets the default pie slice colors. Defaults to
                        the main `colorway` used for trace colors. If
                        you specify a new list here it can still be
                        extended with lighter and darker colors, see
                        `extendpiecolors`.
                    plot_bgcolor
                        Sets the color of plotting area in-between x
                        and y axes.
                    polar
                        plotly.graph_objs.layout.Polar instance or dict
                        with compatible properties
                    radialaxis
                        plotly.graph_objs.layout.RadialAxis instance or
                        dict with compatible properties
                    scene
                        plotly.graph_objs.layout.Scene instance or dict
                        with compatible properties
                    selectdirection
                        When "dragmode" is set to "select", this limits
                        the selection of the drag to horizontal,
                        vertical or diagonal. "h" only allows
                        horizontal selection, "v" only vertical, "d"
                        only diagonal and "any" sets no limit.
                    selectionrevision
                        Controls persistence of user-driven changes in
                        selected points from all traces.
                    separators
                        Sets the decimal and thousand separators. For
                        example, *. * puts a '.' before decimals and a
                        space between thousands. In English locales,
                        dflt is ".," but other locales may alter this
                        default.
                    shapes
                        plotly.graph_objs.layout.Shape instance or dict
                        with compatible properties
                    shapedefaults
                        When used in a template (as
                        layout.template.layout.shapedefaults), sets the
                        default property values to use for elements of
                        layout.shapes
                    showlegend
                        Determines whether or not a legend is drawn.
                        Default is `true` if there is a trace to show
                        and any of these: a) Two or more traces would
                        by default be shown in the legend. b) One pie
                        trace is shown in the legend. c) One trace is
                        explicitly given with `showlegend: true`.
                    sliders
                        plotly.graph_objs.layout.Slider instance or
                        dict with compatible properties
                    sliderdefaults
                        When used in a template (as
                        layout.template.layout.sliderdefaults), sets
                        the default property values to use for elements
                        of layout.sliders
                    spikedistance
                        Sets the default distance (in pixels) to look
                        for data to draw spikelines to (-1 means no
                        cutoff, 0 means no looking for data). As with
                        hoverdistance, distance does not apply to area-
                        like objects. In addition, some objects can be
                        hovered on but will not generate spikelines,
                        such as scatter fills.
                    sunburstcolorway
                        Sets the default sunburst slice colors.
                        Defaults to the main `colorway` used for trace
                        colors. If you specify a new list here it can
                        still be extended with lighter and darker
                        colors, see `extendsunburstcolors`.
                    template
                        Default attributes to be applied to the plot.
                        This should be a dict with format: `{'layout':
                        layoutTemplate, 'data': {trace_type:
                        [traceTemplate, ...], ...}}` where
                        `layoutTemplate` is a dict matching the
                        structure of `figure.layout` and
                        `traceTemplate` is a dict matching the
                        structure of the trace with type `trace_type`
                        (e.g. 'scatter'). Alternatively, this may be
                        specified as an instance of
                        plotly.graph_objs.layout.Template.  Trace
                        templates are applied cyclically to traces of
                        each type. Container arrays (eg `annotations`)
                        have special handling: An object ending in
                        `defaults` (eg `annotationdefaults`) is applied
                        to each array item. But if an item has a
                        `templateitemname` key we look in the template
                        array for an item with matching `name` and
                        apply that instead. If no matching `name` is
                        found we mark the item invisible. Any named
                        template item not referenced is appended to the
                        end of the array, so this can be used to add a
                        watermark annotation or a logo image, for
                        example. To omit one of these items on the
                        plot, make an item with matching
                        `templateitemname` and `visible: false`.
                    ternary
                        plotly.graph_objs.layout.Ternary instance or
                        dict with compatible properties
                    title
                        plotly.graph_objs.layout.Title instance or dict
                        with compatible properties
                    titlefont
                        Deprecated: Please use layout.title.font
                        instead. Sets the title font. Note that the
                        title's font used to be customized by the now
                        deprecated `titlefont` attribute.
                    transition
                        Sets transition options used during
                        Plotly.react updates.
                    uirevision
                        Used to allow user interactions with the plot
                        to persist after `Plotly.react` calls that are
                        unaware of these interactions. If `uirevision`
                        is omitted, or if it is given and it changed
                        from the previous `Plotly.react` call, the
                        exact new figure is used. If `uirevision` is
                        truthy and did NOT change, any attribute that
                        has been affected by user interactions and did
                        not receive a different value in the new figure
                        will keep the interaction value.
                        `layout.uirevision` attribute serves as the
                        default for `uirevision` attributes in various
                        sub-containers. For finer control you can set
                        these sub-attributes directly. For example, if
                        your app separately controls the data on the x
                        and y axes you might set
                        `xaxis.uirevision=*time*` and
                        `yaxis.uirevision=*cost*`. Then if only the y
                        data is changed, you can update
                        `yaxis.uirevision=*quantity*` and the y axis
                        range will reset but the x axis range will
                        retain any user-driven zoom.
                    updatemenus
                        plotly.graph_objs.layout.Updatemenu instance or
                        dict with compatible properties
                    updatemenudefaults
                        When used in a template (as
                        layout.template.layout.updatemenudefaults),
                        sets the default property values to use for
                        elements of layout.updatemenus
                    violingap
                        Sets the gap (in plot fraction) between violins
                        of adjacent location coordinates. Has no effect
                        on traces that have "width" set.
                    violingroupgap
                        Sets the gap (in plot fraction) between violins
                        of the same location coordinate. Has no effect
                        on traces that have "width" set.
                    violinmode
                        Determines how violins at the same location
                        coordinate are displayed on the graph. If
                        "group", the violins are plotted next to one
                        another centered around the shared location. If
                        "overlay", the violins are plotted over one
                        another, you might need to set "opacity" to see
                        them multiple violins. Has no effect on traces
                        that have "width" set.
                    waterfallgap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    waterfallgroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    waterfallmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "group", the bars are plotted next to one
                        another centered around the shared location.
                        With "overlay", the bars are plotted over one
                        another, you might need to an "opacity" to see
                        multiple bars.
                    width
                        Sets the plot's width (in px).
                    xaxis
                        plotly.graph_objs.layout.XAxis instance or dict
                        with compatible properties
                    yaxis
                        plotly.graph_objs.layout.YAxis instance or dict
                        with compatible properties
            
        frames
            The 'frames' property is a tuple of instances of
            Frame that may be specified as:
              - A list or tuple of instances of plotly.graph_objs.Frame
              - A list or tuple of dicts of string/value properties that
                will be passed to the Frame constructor
        
                Supported dict properties:
                    
                    baseframe
                        The name of the frame into which this frame's
                        properties are merged before applying. This is
                        used to unify properties and avoid needing to
                        specify the same values for the same properties
                        in multiple frames.
                    data
                        A list of traces this frame modifies. The
                        format is identical to the normal trace
                        definition.
                    group
                        An identifier that specifies the group to which
                        the frame belongs, used by animate to select a
                        subset of frames.
                    layout
                        Layout properties which this frame modifies.
                        The format is identical to the normal layout
                        definition.
                    name
                        A label by which to identify the frame
                    traces
                        A list of trace indices that identify the
                        respective traces in the data attribute
            
        skip_invalid: bool
            If True, invalid properties in the figure specification will be
            skipped silently. If False (default) invalid properties in the
            figure specification will result in a ValueError

        Raises
        ------
        ValueError
            if a property in the specification of data, layout, or frames
            is invalid AND skip_invalid is False
        """
        super(FigureWidget,
              self).__init__(data, layout, frames, skip_invalid, **kwargs)

    def add_area(
        self,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        r=None,
        rsrc=None,
        showlegend=None,
        stream=None,
        t=None,
        tsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Area trace
        
        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.area.Hoverlabel instance or dict with
            compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.area.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the radial coordinates for
            legacy polar chart only.
        rsrc
            Sets the source reference on plot.ly for  r .
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.area.Stream instance or dict with
            compatible properties
        t
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the angular coordinates for
            legacy polar chart only.
        tsrc
            Sets the source reference on plot.ly for  t .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Area
        """
        new_trace = Area(
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            r=r,
            rsrc=rsrc,
            showlegend=showlegend,
            stream=stream,
            t=t,
            tsrc=tsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_bar(
        self,
        alignmentgroup=None,
        base=None,
        basesrc=None,
        cliponaxis=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        r=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        t=None,
        text=None,
        textangle=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        tsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Bar trace
        
        The data visualized by the span of the bars is set in `y` if
        `orientation` is set th "v" (the default) and the labels are
        set in `x`. By setting `orientation` to "h", the roles are
        interchanged.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        base
            Sets where the bar base is drawn (in position axis
            units). In "stack" or "relative" barmode, traces that
            set "base" will be excluded and drawn in "overlay" mode
            instead.
        basesrc
            Sets the source reference on plot.ly for  base .
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            plotly.graph_objs.bar.ErrorX instance or dict with
            compatible properties
        error_y
            plotly.graph_objs.bar.ErrorY instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.bar.Hoverlabel instance or dict with
            compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.bar.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        r
            r coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the radial
            coordinatesfor legacy polar chart only.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.bar.Selected instance or dict with
            compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.bar.Stream instance or dict with
            compatible properties
        t
            t coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the
            angular coordinatesfor legacy polar chart only.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        tsrc
            Sets the source reference on plot.ly for  t .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.bar.Unselected instance or dict with
            compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        widthsrc
            Sets the source reference on plot.ly for  width .
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Bar
        """
        new_trace = Bar(
            alignmentgroup=alignmentgroup,
            base=base,
            basesrc=basesrc,
            cliponaxis=cliponaxis,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            offsetsrc=offsetsrc,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            r=r,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            t=t,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            tsrc=tsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_barpolar(
        self,
        base=None,
        basesrc=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetsrc=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Barpolar trace
        
        The data visualized by the radial span of the bars is set in
        `r`

        Parameters
        ----------
        base
            Sets where the bar base is drawn (in radial axis
            units). In "stack" barmode, traces that set "base" will
            be excluded and drawn in "overlay" mode instead.
        basesrc
            Sets the source reference on plot.ly for  base .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.barpolar.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.barpolar.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the angular position where the bar is drawn (in
            "thetatunit" units).
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.barpolar.Selected instance or dict
            with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.barpolar.Stream instance or dict with
            compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets hover text elements associated with each bar. If a
            single string, the same string appears over all bars.
            If an array of string, the items are mapped in order to
            the this trace's coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on plot.ly for  theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.barpolar.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar angular width (in "thetaunit" units).
        widthsrc
            Sets the source reference on plot.ly for  width .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Barpolar
        """
        new_trace = Barpolar(
            base=base,
            basesrc=basesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetsrc=offsetsrc,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_box(
        self,
        alignmentgroup=None,
        boxmean=None,
        boxpoints=None,
        customdata=None,
        customdatasrc=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        notched=None,
        notchwidth=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        whiskerwidth=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Box trace
        
        In vertical (horizontal) box plots, statistics are computed
        using `y` (`x`) values. By supplying an `x` (`y`) array, one
        box per distinct x (y) value is drawn If no `x` (`y`) list is
        provided, a single box is drawn. That box position is then
        positioned with with `name` or with `x0` (`y0`) if provided.
        Each box spans from quartile 1 (Q1) to quartile 3 (Q3). The
        second quartile (Q2) is marked by a line inside the box. By
        default, the whiskers correspond to the box' edges +/- 1.5
        times the interquartile range (IQR: Q3-Q1), see "boxpoints" for
        other options.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        boxmean
            If True, the mean of the box(es)' underlying
            distribution is drawn as a dashed line inside the
            box(es). If "sd" the standard deviation is also drawn.
        boxpoints
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the box(es) are shown with no sample
            points
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.box.Hoverlabel instance or dict with
            compatible properties
        hoveron
            Do the hover effects highlight individual boxes  or
            sample points or both?
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the box(es).
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.box.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.box.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For box traces, the name will
            also be used for the position coordinate, if `x` and
            `x0` (`y` and `y0` if horizontal) are missing and the
            position axis is categorical
        notched
            Determines whether or not notches should be drawn.
        notchwidth
            Sets the width of the notches relative to the box'
            width. For example, with 0, the notches are as wide as
            the box(es).
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the box(es). If "v" ("h"), the
            distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the box(es). If 0, the sample points are places over
            the center of the box(es). Positive (negative) values
            correspond to positions to the right (left) for
            vertical boxes and above (below) for horizontal boxes
        selected
            plotly.graph_objs.box.Selected instance or dict with
            compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.box.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.box.Unselected instance or dict with
            compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        whiskerwidth
            Sets the width of the whiskers relative to the box'
            width. For example, with 1, the whiskers are as wide as
            the box(es).
        width
            Sets the width of the box in data coordinate If 0
            (default value) the width is automatically selected
            based on the positions of other box traces in the same
            subplot.
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate of the box. See overview for more
            info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate of the box. See overview for more
            info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Box
        """
        new_trace = Box(
            alignmentgroup=alignmentgroup,
            boxmean=boxmean,
            boxpoints=boxpoints,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            jitter=jitter,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            notched=notched,
            notchwidth=notchwidth,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            pointpos=pointpos,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            whiskerwidth=whiskerwidth,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_candlestick(
        self,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legendgroup=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        whiskerwidth=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        yaxis=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Candlestick trace
        
        The candlestick is a style of financial chart describing open,
        high, low and close for a given `x` coordinate (most likely
        time). The boxes represent the spread between the `open` and
        `close` values and the lines represent the spread between the
        `low` and `high` values Sample points where the close value is
        higher (lower) then the open value are called increasing
        (decreasing). By default, increasing candles are drawn in green
        whereas decreasing are drawn in red.

        Parameters
        ----------
        close
            Sets the close values.
        closesrc
            Sets the source reference on plot.ly for  close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        decreasing
            plotly.graph_objs.candlestick.Decreasing instance or
            dict with compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on plot.ly for  high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.candlestick.Hoverlabel instance or
            dict with compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        increasing
            plotly.graph_objs.candlestick.Increasing instance or
            dict with compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.candlestick.Line instance or dict
            with compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on plot.ly for  low .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on plot.ly for  open .
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.candlestick.Stream instance or dict
            with compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        whiskerwidth
            Sets the width of the whiskers relative to the box'
            width. For example, with 1, the whiskers are as wide as
            the box(es).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Candlestick
        """
        new_trace = Candlestick(
            close=close,
            closesrc=closesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            high=high,
            highsrc=highsrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            legendgroup=legendgroup,
            line=line,
            low=low,
            lowsrc=lowsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            open=open,
            opensrc=opensrc,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            whiskerwidth=whiskerwidth,
            x=x,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            yaxis=yaxis,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_carpet(
        self,
        a=None,
        a0=None,
        aaxis=None,
        asrc=None,
        b=None,
        b0=None,
        baxis=None,
        bsrc=None,
        carpet=None,
        cheaterslope=None,
        color=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        font=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Carpet trace
        
        The data describing carpet axis layout is set in `y` and
        (optionally) also `x`. If only `y` is present, `x` the plot is
        interpreted as a cheater plot and is filled in using the `y`
        values. `x` and `y` may either be 2D arrays matching with each
        dimension matching that of `a` and `b`, or they may be 1D
        arrays with total length equal to that of `a` and `b`.

        Parameters
        ----------
        a
            An array containing values of the first parameter value
        a0
            Alternate to `a`. Builds a linear space of a
            coordinates. Use with `da` where `a0` is the starting
            coordinate and `da` the step.
        aaxis
            plotly.graph_objs.carpet.Aaxis instance or dict with
            compatible properties
        asrc
            Sets the source reference on plot.ly for  a .
        b
            A two dimensional array of y coordinates at each carpet
            point.
        b0
            Alternate to `b`. Builds a linear space of a
            coordinates. Use with `db` where `b0` is the starting
            coordinate and `db` the step.
        baxis
            plotly.graph_objs.carpet.Baxis instance or dict with
            compatible properties
        bsrc
            Sets the source reference on plot.ly for  b .
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `scattercontour` traces can specify a carpet plot
            on which they lie
        cheaterslope
            The shift applied to each successive row of data in
            creating a cheater plot. Only used if `x` is been
            ommitted.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        da
            Sets the a coordinate step. See `a0` for more info.
        db
            Sets the b coordinate step. See `b0` for more info.
        font
            The default font used for axis & tick labels on this
            carpet
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.carpet.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        stream
            plotly.graph_objs.carpet.Stream instance or dict with
            compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            A two dimensional array of x coordinates at each carpet
            point. If ommitted, the plot is a cheater plot and the
            xaxis is hidden by default.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            A two dimensional array of y coordinates at each carpet
            point.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Carpet
        """
        new_trace = Carpet(
            a=a,
            a0=a0,
            aaxis=aaxis,
            asrc=asrc,
            b=b,
            b0=b0,
            baxis=baxis,
            bsrc=bsrc,
            carpet=carpet,
            cheaterslope=cheaterslope,
            color=color,
            customdata=customdata,
            customdatasrc=customdatasrc,
            da=da,
            db=db,
            font=font,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_choropleth(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        geo=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        locationmode=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Choropleth trace
        
        The data that describes the choropleth value-to-color mapping
        is set in `z`. The geographic locations corresponding to each
        value in `z` are set in `locations`.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.choropleth.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        geo
            Sets a reference between this trace's geospatial
            coordinates and a geographic map. If "geo" (the default
            value), the geospatial coordinates refer to
            `layout.geo`. If "geo2", the geospatial coordinates
            refer to `layout.geo2`, and so on.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.choropleth.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        locationmode
            Determines the set of locations used to match entries
            in `locations` to regions on the map.
        locations
            Sets the coordinates via location IDs or names. See
            `locationmode` for more info.
        locationssrc
            Sets the source reference on plot.ly for  locations .
        marker
            plotly.graph_objs.choropleth.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        selected
            plotly.graph_objs.choropleth.Selected instance or dict
            with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.choropleth.Stream instance or dict
            with compatible properties
        text
            Sets the text elements associated with each location.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.choropleth.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        z
            Sets the color values.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Choropleth
        """
        new_trace = Choropleth(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            geo=geo,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            locationmode=locationmode,
            locations=locations,
            locationssrc=locationssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            reversescale=reversescale,
            selected=selected,
            selectedpoints=selectedpoints,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_cone(
        self,
        anchor=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showscale=None,
        sizemode=None,
        sizeref=None,
        stream=None,
        text=None,
        textsrc=None,
        u=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        visible=None,
        vsrc=None,
        w=None,
        wsrc=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Cone trace
        
        Use cone traces to visualize vector fields.  Specify a vector
        field using 6 1D arrays, 3 position arrays `x`, `y` and `z` and
        3 vector component arrays `u`, `v`, `w`. The cones are drawn
        exactly at the positions given by `x`, `y` and `z`.

        Parameters
        ----------
        anchor
            Sets the cones' anchor with respect to their x/y/z
            positions. Note that "cm" denote the cone's center of
            mass which corresponds to 1/4 from the tail to tip.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here u/v/w norm) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as u/v/w norm. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.cone.ColorBar instance or dict with
            compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.cone.Hoverlabel instance or dict with
            compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variable `norm` Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        lighting
            plotly.graph_objs.cone.Lighting instance or dict with
            compatible properties
        lightposition
            plotly.graph_objs.cone.Lightposition instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        sizemode
            Determines whether `sizeref` is set as a "scaled" (i.e
            unitless) scalar (normalized by the max u/v/w norm in
            the vector field) or as "absolute" value (in the same
            units as the vector field).
        sizeref
            Adjusts the cone size scaling. The size of the cones is
            determined by their u/v/w norm multiplied a factor and
            `sizeref`. This factor (computed internally)
            corresponds to the minimum "time" to travel across two
            successive x/y/z positions at the average velocity of
            those two successive positions. All cones in a given
            trace use the same factor. With `sizemode` set to
            "scaled", `sizeref` is unitless, its default value is
            0.5 With `sizemode` set to "absolute", `sizeref` has
            the same units as the u/v/w vector field, its the
            default value is half the sample's maximum vector norm.
        stream
            plotly.graph_objs.cone.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with the cones. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        u
            Sets the x components of the vector field.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        usrc
            Sets the source reference on plot.ly for  u .
        v
            Sets the y components of the vector field.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        vsrc
            Sets the source reference on plot.ly for  v .
        w
            Sets the z components of the vector field.
        wsrc
            Sets the source reference on plot.ly for  w .
        x
            Sets the x coordinates of the vector field and of the
            displayed cones.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates of the vector field and of the
            displayed cones.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the z coordinates of the vector field and of the
            displayed cones.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Cone
        """
        new_trace = Cone(
            anchor=anchor,
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showscale=showscale,
            sizemode=sizemode,
            sizeref=sizeref,
            stream=stream,
            text=text,
            textsrc=textsrc,
            u=u,
            uid=uid,
            uirevision=uirevision,
            usrc=usrc,
            v=v,
            visible=visible,
            vsrc=vsrc,
            w=w,
            wsrc=wsrc,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_contour(
        self,
        autocolorscale=None,
        autocontour=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Contour trace
        
        The data from which contour lines are computed is set in `z`.
        Data in `z` must be a 2D list of numbers. Say that `z` has N
        rows and M columns, then by default, these N rows correspond to
        N y coordinates (set in `y` or auto-generated) and the M
        columns correspond to M x coordinates (set in `x` or auto-
        generated). By setting `transpose` to True, the above behavior
        is flipped.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If True, the number of
            contour levels can be set in `ncontours`. If False, set
            the contour level attributes in `contours`.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.contour.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in.
        contours
            plotly.graph_objs.contour.Contours instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        fillcolor
            Sets the fill color if `contours.type` is "constraint".
            Defaults to a half-transparent variant of the line
            color, marker color, or marker line color, whichever is
            available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.contour.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.contour.Line instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is True or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.contour.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on plot.ly for  text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        xtype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        ytype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Contour
        """
        new_trace = Contour(
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_contourcarpet(
        self,
        a=None,
        a0=None,
        asrc=None,
        atype=None,
        autocolorscale=None,
        autocontour=None,
        b=None,
        b0=None,
        bsrc=None,
        btype=None,
        carpet=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Contourcarpet trace
        
        Plots contours on either the first carpet axis or the carpet
        axis with a matching `carpet` attribute. Data `z` is
        interpreted as matching that of the corresponding carpet axis.

        Parameters
        ----------
        a
            Sets the x coordinates.
        a0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        asrc
            Sets the source reference on plot.ly for  a .
        atype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If True, the number of
            contour levels can be set in `ncontours`. If False, set
            the contour level attributes in `contours`.
        b
            Sets the y coordinates.
        b0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        bsrc
            Sets the source reference on plot.ly for  b .
        btype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        carpet
            The `carpet` of the carpet axes on which this contour
            trace lies
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.contourcarpet.ColorBar instance or
            dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contours
            plotly.graph_objs.contourcarpet.Contours instance or
            dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        da
            Sets the x coordinate step. See `x0` for more info.
        db
            Sets the y coordinate step. See `y0` for more info.
        fillcolor
            Sets the fill color if `contours.type` is "constraint".
            Defaults to a half-transparent variant of the line
            color, marker color, or marker line color, whichever is
            available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.contourcarpet.Hoverlabel instance or
            dict with compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.contourcarpet.Line instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is True or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.contourcarpet.Stream instance or dict
            with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on plot.ly for  text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Contourcarpet
        """
        new_trace = Contourcarpet(
            a=a,
            a0=a0,
            asrc=asrc,
            atype=atype,
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            b=b,
            b0=b0,
            bsrc=bsrc,
            btype=btype,
            carpet=carpet,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            da=da,
            db=db,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            xaxis=xaxis,
            yaxis=yaxis,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_funnel(
        self,
        alignmentgroup=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Funnel trace
        
        Visualize stages in a process using length-encoded bars. This
        trace can be used to show data in either a part-to-whole
        representation wherein each item appears in a single stage, or
        in a "drop-off" representation wherein each item appears in
        each stage it traversed. See also the "funnelarea" trace type
        for a different approach to visualizing funnel data.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        connector
            plotly.graph_objs.funnel.Connector instance or dict
            with compatible properties
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.funnel.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.funnel.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the funnels. With "v" ("h"),
            the value of the each bar spans along the vertical
            (horizontal). By default funnels are tend to be
            oriented horizontally; unless only "y" array is
            presented or orientation is set to "v". Also regarding
            graphs including only 'horizontal' funnels, "autorange"
            on the "y-axis" are set to "reversed".
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.funnel.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textinfo
            Determines which trace information appear on the graph.
            In the case of having multiple funnels, percentages &
            totals are computed separately (per trace).
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Funnel
        """
        new_trace = Funnel(
            alignmentgroup=alignmentgroup,
            cliponaxis=cliponaxis,
            connector=connector,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_funnelarea(
        self,
        aspectratio=None,
        baseratio=None,
        customdata=None,
        customdatasrc=None,
        dlabel=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        scalegroup=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        title=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Funnelarea trace
        
        Visualize stages in a process using area-encoded trapezoids.
        This trace can be used to show data in a part-to-whole
        representation similar to a "pie" trace, wherein each item
        appears in a single stage. See also the "funnel" trace type for
        a different approach to visualizing funnel data.

        Parameters
        ----------
        aspectratio
            Sets the ratio between height and width
        baseratio
            Sets the ratio between bottom length and maximum top
            length.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dlabel
            Sets the label step. See `label0` for more info.
        domain
            plotly.graph_objs.funnelarea.Domain instance or dict
            with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.funnelarea.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variables `label`, `color`, `value`,
            `percent` and `text`. Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        label0
            Alternate to `labels`. Builds a numeric set of labels.
            Use with `dlabel` where `label0` is the starting label
            and `dlabel` the step.
        labels
            Sets the sector labels. If `labels` entries are
            duplicated, we sum associated `values` or simply count
            occurrences if `values` is not provided. For other
            array attributes (including color) we use the first
            non-empty entry among all occurrences of the label.
        labelssrc
            Sets the source reference on plot.ly for  labels .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.funnelarea.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        scalegroup
            If there are multiple funnelareas that should be sized
            according to their totals, link them by providing a
            non-empty group id here shared by every trace in the
            same group.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.funnelarea.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Specifies the location of the `textinfo`.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        title
            plotly.graph_objs.funnelarea.Title instance or dict
            with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values of the sectors. If omitted, we count
            occurrences of each label.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Funnelarea
        """
        new_trace = Funnelarea(
            aspectratio=aspectratio,
            baseratio=baseratio,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dlabel=dlabel,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            label0=label0,
            labels=labels,
            labelssrc=labelssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            scalegroup=scalegroup,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            title=title,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_heatmap(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xgap=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ygap=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Heatmap trace
        
        The data that describes the heatmap value-to-color mapping is
        set in `z`. Data in `z` can either be a 2D list of values
        (ragged or not) or a 1D array of values. In the case where `z`
        is a 2D list, say that `z` has N rows and M columns. Then, by
        default, the resulting heatmap will have N partitions along the
        y axis and M partitions along the x axis. In other words, the
        i-th row/ j-th column cell in `z` is mapped to the i-th
        partition of the y axis (starting from the bottom of the plot)
        and the j-th partition of the x-axis (starting from the left of
        the plot). This behavior can be flipped by using `transpose`.
        Moreover, `x` (`y`) can be provided with M or M+1 (N or N+1)
        elements. If M (N), then the coordinates correspond to the
        center of the heatmap cells and the cells have equal width. If
        M+1 (N+1), then the coordinates correspond to the edges of the
        heatmap cells. In the case where `z` is a 1D list, the x and y
        coordinates must be provided in `x` and `y` respectively to
        form data triplets.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.heatmap.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.heatmap.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.heatmap.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on plot.ly for  text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xgap
            Sets the horizontal gap (in pixels) between bricks.
        xsrc
            Sets the source reference on plot.ly for  x .
        xtype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ygap
            Sets the vertical gap (in pixels) between bricks.
        ysrc
            Sets the source reference on plot.ly for  y .
        ytype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsmooth
            Picks a smoothing algorithm use to smooth `z` data.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Heatmap
        """
        new_trace = Heatmap(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xgap=xgap,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ygap=ygap,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_heatmapgl(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Heatmapgl trace
        
        WebGL version of the heatmap trace type.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.heatmapgl.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.heatmapgl.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.heatmapgl.Stream instance or dict
            with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on plot.ly for  text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        xtype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .
        ytype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Heatmapgl
        """
        new_trace = Heatmapgl(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_histogram(
        self,
        alignmentgroup=None,
        autobinx=None,
        autobiny=None,
        bingroup=None,
        cumulative=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        xaxis=None,
        xbins=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybins=None,
        ycalendar=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Histogram trace
        
        The sample data from which statistics are computed is set in
        `x` for vertically spanning histograms and in `y` for
        horizontally spanning histograms. Binning options are set
        `xbins` and `ybins` respectively if no aggregation data is
        provided.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        bingroup
            Set a group of histogram traces which will have
            compatible bin settings. Note that traces on the same
            subplot and with the same "orientation" under `barmode`
            "stack", "relative" and "group" are forced into the
            same bingroup, Using `bingroup`, traces under `barmode`
            "overlay" and on different axes (of the same axis type)
            can have compatible bin settings. Note that histogram
            and histogram2d* trace can share the same `bingroup`
        cumulative
            plotly.graph_objs.histogram.Cumulative instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        error_x
            plotly.graph_objs.histogram.ErrorX instance or dict
            with compatible properties
        error_y
            plotly.graph_objs.histogram.ErrorY instance or dict
            with compatible properties
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.histogram.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variable `binNumber` Anything contained in
            tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.histogram.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        selected
            plotly.graph_objs.histogram.Selected instance or dict
            with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.histogram.Stream instance or dict
            with compatible properties
        text
            Sets hover text elements associated with each bar. If a
            single string, the same string appears over all bars.
            If an array of string, the items are mapped in order to
            the this trace's coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.histogram.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbins
            plotly.graph_objs.histogram.XBins instance or dict with
            compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybins
            plotly.graph_objs.histogram.YBins instance or dict with
            compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Histogram
        """
        new_trace = Histogram(
            alignmentgroup=alignmentgroup,
            autobinx=autobinx,
            autobiny=autobiny,
            bingroup=bingroup,
            cumulative=cumulative,
            customdata=customdata,
            customdatasrc=customdatasrc,
            error_x=error_x,
            error_y=error_y,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbins=xbins,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybins=ybins,
            ycalendar=ycalendar,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_histogram2d(
        self,
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        opacity=None,
        reversescale=None,
        showscale=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xgap=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        ygap=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Histogram2d trace
        
        The sample data from which statistics are computed is set in
        `x` and `y` (where `x` and `y` represent marginal
        distributions, binning is set in `xbins` and `ybins` in this
        case) or `z` (where `z` represent the 2D distribution and
        binning set, binning is set by `x` and `y` in this case). The
        resulting distribution is visualized as a heatmap.

        Parameters
        ----------
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        bingroup
            Set the `xbingroup` and `ybingroup` default prefix For
            example, setting a `bingroup` of 1 on two histogram2d
            traces will make them their x-bins and y-bins match
            separately.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.histogram2d.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.histogram2d.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variable `z` Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        marker
            plotly.graph_objs.histogram2d.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.histogram2d.Stream instance or dict
            with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbingroup
            Set a group of histogram traces which will have
            compatible x-bin settings. Using `xbingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible x-bin settings.
            Note that the same `xbingroup` value can be used to set
            (1D) histogram `bingroup`
        xbins
            plotly.graph_objs.histogram2d.XBins instance or dict
            with compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xgap
            Sets the horizontal gap (in pixels) between bricks.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybingroup
            Set a group of histogram traces which will have
            compatible y-bin settings. Using `ybingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible y-bin settings.
            Note that the same `ybingroup` value can be used to set
            (1D) histogram `bingroup`
        ybins
            plotly.graph_objs.histogram2d.YBins instance or dict
            with compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ygap
            Sets the vertical gap (in pixels) between bricks.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the aggregation data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsmooth
            Picks a smoothing algorithm use to smooth `z` data.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Histogram2d
        """
        new_trace = Histogram2d(
            autobinx=autobinx,
            autobiny=autobiny,
            autocolorscale=autocolorscale,
            bingroup=bingroup,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            ids=ids,
            idssrc=idssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            opacity=opacity,
            reversescale=reversescale,
            showscale=showscale,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbingroup=xbingroup,
            xbins=xbins,
            xcalendar=xcalendar,
            xgap=xgap,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybingroup=ybingroup,
            ybins=ybins,
            ycalendar=ycalendar,
            ygap=ygap,
            ysrc=ysrc,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_histogram2dcontour(
        self,
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        autocontour=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Histogram2dContour trace
        
        The sample data from which statistics are computed is set in
        `x` and `y` (where `x` and `y` represent marginal
        distributions, binning is set in `xbins` and `ybins` in this
        case) or `z` (where `z` represent the 2D distribution and
        binning set, binning is set by `x` and `y` in this case). The
        resulting distribution is visualized as a contour plot.

        Parameters
        ----------
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If True, the number of
            contour levels can be set in `ncontours`. If False, set
            the contour level attributes in `contours`.
        bingroup
            Set the `xbingroup` and `ybingroup` default prefix For
            example, setting a `bingroup` of 1 on two histogram2d
            traces will make them their x-bins and y-bins match
            separately.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.histogram2dcontour.ColorBar instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contours
            plotly.graph_objs.histogram2dcontour.Contours instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.histogram2dcontour.Hoverlabel
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variable `z` Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.histogram2dcontour.Line instance or
            dict with compatible properties
        marker
            plotly.graph_objs.histogram2dcontour.Marker instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is True or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.histogram2dcontour.Stream instance or
            dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbingroup
            Set a group of histogram traces which will have
            compatible x-bin settings. Using `xbingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible x-bin settings.
            Note that the same `xbingroup` value can be used to set
            (1D) histogram `bingroup`
        xbins
            plotly.graph_objs.histogram2dcontour.XBins instance or
            dict with compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybingroup
            Set a group of histogram traces which will have
            compatible y-bin settings. Using `ybingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible y-bin settings.
            Note that the same `ybingroup` value can be used to set
            (1D) histogram `bingroup`
        ybins
            plotly.graph_objs.histogram2dcontour.YBins instance or
            dict with compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the aggregation data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Histogram2dContour
        """
        new_trace = Histogram2dContour(
            autobinx=autobinx,
            autobiny=autobiny,
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            bingroup=bingroup,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbingroup=xbingroup,
            xbins=xbins,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybingroup=ybingroup,
            ybins=ybins,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_isosurface(
        self,
        autocolorscale=None,
        caps=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        isomax=None,
        isomin=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showscale=None,
        slices=None,
        spaceframe=None,
        stream=None,
        surface=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        value=None,
        valuesrc=None,
        visible=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Isosurface trace
        
        Draws isosurfaces between iso-min and iso-max values with
        coordinates given by four 1-dimensional arrays containing the
        `value`, `x`, `y` and `z` of every vertex of a uniform or non-
        uniform 3-D grid. Horizontal or vertical slices, caps as well
        as spaceframe between iso-min and iso-max values could also be
        drawn using this trace.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        caps
            plotly.graph_objs.isosurface.Caps instance or dict with
            compatible properties
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `value`) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `value` and if set, `cmin` must
            be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `value`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `value` and if set, `cmax` must
            be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.isosurface.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contour
            plotly.graph_objs.isosurface.Contour instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.isosurface.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        isomax
            Sets the maximum boundary for iso-surface plot.
        isomin
            Sets the minimum boundary for iso-surface plot.
        lighting
            plotly.graph_objs.isosurface.Lighting instance or dict
            with compatible properties
        lightposition
            plotly.graph_objs.isosurface.Lightposition instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        slices
            plotly.graph_objs.isosurface.Slices instance or dict
            with compatible properties
        spaceframe
            plotly.graph_objs.isosurface.Spaceframe instance or
            dict with compatible properties
        stream
            plotly.graph_objs.isosurface.Stream instance or dict
            with compatible properties
        surface
            plotly.graph_objs.isosurface.Surface instance or dict
            with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the 4th dimension (value) of the vertices.
        valuesrc
            Sets the source reference on plot.ly for  value .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices on X axis.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the Y coordinates of the vertices on Y axis.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the Z coordinates of the vertices on Z axis.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Isosurface
        """
        new_trace = Isosurface(
            autocolorscale=autocolorscale,
            caps=caps,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            isomax=isomax,
            isomin=isomin,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showscale=showscale,
            slices=slices,
            spaceframe=spaceframe,
            stream=stream,
            surface=surface,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            value=value,
            valuesrc=valuesrc,
            visible=visible,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_mesh3d(
        self,
        alphahull=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        color=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        delaunayaxis=None,
        facecolor=None,
        facecolorsrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        i=None,
        ids=None,
        idssrc=None,
        intensity=None,
        intensitysrc=None,
        isrc=None,
        j=None,
        jsrc=None,
        k=None,
        ksrc=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        vertexcolor=None,
        vertexcolorsrc=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Mesh3d trace
        
        Draws sets of triangles with coordinates given by three
        1-dimensional arrays in `x`, `y`, `z` and (1) a sets of `i`,
        `j`, `k` indices (2) Delaunay triangulation or (3) the Alpha-
        shape algorithm or (4) the Convex-hull algorithm

        Parameters
        ----------
        alphahull
            Determines how the mesh surface triangles are derived
            from the set of vertices (points) represented by the
            `x`, `y` and `z` arrays, if the `i`, `j`, `k` arrays
            are not supplied. For general use of `mesh3d` it is
            preferred that `i`, `j`, `k` are supplied. If "-1",
            Delaunay triangulation is used, which is mainly
            suitable if the mesh is a single, more or less layer
            surface that is perpendicular to `delaunayaxis`. In
            case the `delaunayaxis` intersects the mesh surface at
            more than one point it will result triangles that are
            very long in the dimension of `delaunayaxis`. If ">0",
            the alpha-shape algorithm is used. In this case, the
            positive `alphahull` value signals the use of the
            alpha-shape algorithm, _and_ its value acts as the
            parameter for the mesh fitting. If 0,  the convex-hull
            algorithm is used. It is suitable for convex bodies or
            if the intention is to enclose the `x`, `y` and `z`
            point set into a convex hull.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `intensity`) or
            the bounds set in `cmin` and `cmax`  Defaults to
            `false` when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `intensity`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmax`
            must be set as well.
        color
            Sets the color of the whole mesh
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.mesh3d.ColorBar instance or dict with
            compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contour
            plotly.graph_objs.mesh3d.Contour instance or dict with
            compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        delaunayaxis
            Sets the Delaunay axis, which is the axis that is
            perpendicular to the surface of the Delaunay
            triangulation. It has an effect if `i`, `j`, `k` are
            not provided and `alphahull` is set to indicate
            Delaunay triangulation.
        facecolor
            Sets the color of each face Overrides "color" and
            "vertexcolor".
        facecolorsrc
            Sets the source reference on plot.ly for  facecolor .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.mesh3d.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        i
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "first" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `i[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `i` represents a point in space, which
            is the first vertex of a triangle.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        intensity
            Sets the vertex intensity values, used for plotting
            fields on meshes
        intensitysrc
            Sets the source reference on plot.ly for  intensity .
        isrc
            Sets the source reference on plot.ly for  i .
        j
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "second" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}`  together represent face m (triangle m) in
            the mesh, where `j[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `j` represents a point in space, which
            is the second vertex of a triangle.
        jsrc
            Sets the source reference on plot.ly for  j .
        k
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "third" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `k[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `k` represents a point in space, which
            is the third vertex of a triangle.
        ksrc
            Sets the source reference on plot.ly for  k .
        lighting
            plotly.graph_objs.mesh3d.Lighting instance or dict with
            compatible properties
        lightposition
            plotly.graph_objs.mesh3d.Lightposition instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.mesh3d.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        vertexcolor
            Sets the color of each vertex Overrides "color". While
            Red, green and blue colors are in the range of 0 and
            255; in the case of having vertex color data in RGBA
            format, the alpha color should be normalized to be
            between 0 and 1.
        vertexcolorsrc
            Sets the source reference on plot.ly for  vertexcolor .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the Y coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the Z coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Mesh3d
        """
        new_trace = Mesh3d(
            alphahull=alphahull,
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            color=color,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            delaunayaxis=delaunayaxis,
            facecolor=facecolor,
            facecolorsrc=facecolorsrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            i=i,
            ids=ids,
            idssrc=idssrc,
            intensity=intensity,
            intensitysrc=intensitysrc,
            isrc=isrc,
            j=j,
            jsrc=jsrc,
            k=k,
            ksrc=ksrc,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            vertexcolor=vertexcolor,
            vertexcolorsrc=vertexcolorsrc,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_ohlc(
        self,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legendgroup=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        tickwidth=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        yaxis=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Ohlc trace
        
        The ohlc (short for Open-High-Low-Close) is a style of
        financial chart describing open, high, low and close for a
        given `x` coordinate (most likely time). The tip of the lines
        represent the `low` and `high` values and the horizontal
        segments represent the `open` and `close` values. Sample points
        where the close value is higher (lower) then the open value are
        called increasing (decreasing). By default, increasing items
        are drawn in green whereas decreasing are drawn in red.

        Parameters
        ----------
        close
            Sets the close values.
        closesrc
            Sets the source reference on plot.ly for  close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        decreasing
            plotly.graph_objs.ohlc.Decreasing instance or dict with
            compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on plot.ly for  high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.ohlc.Hoverlabel instance or dict with
            compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        increasing
            plotly.graph_objs.ohlc.Increasing instance or dict with
            compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.ohlc.Line instance or dict with
            compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on plot.ly for  low .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on plot.ly for  open .
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.ohlc.Stream instance or dict with
            compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on plot.ly for  text .
        tickwidth
            Sets the width of the open/close tick marks relative to
            the "x" minimal interval.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Ohlc
        """
        new_trace = Ohlc(
            close=close,
            closesrc=closesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            high=high,
            highsrc=highsrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            legendgroup=legendgroup,
            line=line,
            low=low,
            lowsrc=lowsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            open=open,
            opensrc=opensrc,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            tickwidth=tickwidth,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            yaxis=yaxis,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_parcats(
        self,
        arrangement=None,
        bundlecolors=None,
        counts=None,
        countssrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        hoverinfo=None,
        hoveron=None,
        hovertemplate=None,
        labelfont=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        sortpaths=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Parcats trace
        
        Parallel categories diagram for multidimensional categorical
        data.

        Parameters
        ----------
        arrangement
            Sets the drag interaction mode for categories and
            dimensions. If `perpendicular`, the categories can only
            move along a line perpendicular to the paths. If
            `freeform`, the categories can freely move on the
            plane. If `fixed`, the categories and dimensions are
            stationary.
        bundlecolors
            Sort paths so that like colors are bundled together
            within each category.
        counts
            The number of observations represented by each state.
            Defaults to 1 so that each state represents one
            observation
        countssrc
            Sets the source reference on plot.ly for  counts .
        dimensions
            The dimensions (variables) of the parallel categories
            diagram.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcats.dimensiondefaults), sets
            the default property values to use for elements of
            parcats.dimensions
        domain
            plotly.graph_objs.parcats.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoveron
            Sets the hover interaction mode for the parcats
            diagram. If `category`, hover interaction take place
            per category. If `color`, hover interactions take place
            per color per category. If `dimension`, hover
            interactions take place across all categories per
            dimension.
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variables `count`, `probability`,
            `category`, `categorycount`, `colorcount` and
            `bandcolorcount`. Anything contained in tag `<extra>`
            is displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        labelfont
            Sets the font for the `dimension` labels.
        line
            plotly.graph_objs.parcats.Line instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        sortpaths
            Sets the path sorting algorithm. If `forward`, sort
            paths based on dimension categories from left to right.
            If `backward`, sort paths based on dimensions
            categories from right to left.
        stream
            plotly.graph_objs.parcats.Stream instance or dict with
            compatible properties
        tickfont
            Sets the font for the `category` labels.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Parcats
        """
        new_trace = Parcats(
            arrangement=arrangement,
            bundlecolors=bundlecolors,
            counts=counts,
            countssrc=countssrc,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            domain=domain,
            hoverinfo=hoverinfo,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            labelfont=labelfont,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            sortpaths=sortpaths,
            stream=stream,
            tickfont=tickfont,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_parcoords(
        self,
        customdata=None,
        customdatasrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        ids=None,
        idssrc=None,
        labelfont=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        rangefont=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Parcoords trace
        
        Parallel coordinates for multidimensional exploratory data
        analysis. The samples are specified in `dimensions`. The colors
        are set in `line.color`.

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dimensions
            The dimensions (variables) of the parallel coordinates
            chart. 2..60 dimensions are supported.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcoords.dimensiondefaults), sets
            the default property values to use for elements of
            parcoords.dimensions
        domain
            plotly.graph_objs.parcoords.Domain instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        labelfont
            Sets the font for the `dimension` labels.
        line
            plotly.graph_objs.parcoords.Line instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        rangefont
            Sets the font for the `dimension` range values.
        stream
            plotly.graph_objs.parcoords.Stream instance or dict
            with compatible properties
        tickfont
            Sets the font for the `dimension` tick values.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Parcoords
        """
        new_trace = Parcoords(
            customdata=customdata,
            customdatasrc=customdatasrc,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            domain=domain,
            ids=ids,
            idssrc=idssrc,
            labelfont=labelfont,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            rangefont=rangefont,
            stream=stream,
            tickfont=tickfont,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_pie(
        self,
        customdata=None,
        customdatasrc=None,
        direction=None,
        dlabel=None,
        domain=None,
        hole=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        pull=None,
        pullsrc=None,
        rotation=None,
        scalegroup=None,
        showlegend=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        title=None,
        titlefont=None,
        titleposition=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Pie trace
        
        A data visualized by the sectors of the pie is set in `values`.
        The sector labels are set in `labels`. The sector colors are
        set in `marker.colors`

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        direction
            Specifies the direction at which succeeding sectors
            follow one another.
        dlabel
            Sets the label step. See `label0` for more info.
        domain
            plotly.graph_objs.pie.Domain instance or dict with
            compatible properties
        hole
            Sets the fraction of the radius to cut out of the pie.
            Use this to make a donut chart.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.pie.Hoverlabel instance or dict with
            compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variables `label`, `color`, `value`,
            `percent` and `text`. Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        label0
            Alternate to `labels`. Builds a numeric set of labels.
            Use with `dlabel` where `label0` is the starting label
            and `dlabel` the step.
        labels
            Sets the sector labels. If `labels` entries are
            duplicated, we sum associated `values` or simply count
            occurrences if `values` is not provided. For other
            array attributes (including color) we use the first
            non-empty entry among all occurrences of the label.
        labelssrc
            Sets the source reference on plot.ly for  labels .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.pie.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector.
        pull
            Sets the fraction of larger radius to pull the sectors
            out from the center. This can be a constant to pull all
            slices apart from each other equally or an array to
            highlight one or more slices.
        pullsrc
            Sets the source reference on plot.ly for  pull .
        rotation
            Instead of the first slice starting at 12 o'clock,
            rotate to some other angle.
        scalegroup
            If there are multiple pie charts that should be sized
            according to their totals, link them by providing a
            non-empty group id here shared by every trace in the
            same group.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            plotly.graph_objs.pie.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Specifies the location of the `textinfo`.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        title
            plotly.graph_objs.pie.Title instance or dict with
            compatible properties
        titlefont
            Deprecated: Please use pie.title.font instead. Sets the
            font used for `title`. Note that the title's font used
            to be set by the now deprecated `titlefont` attribute.
        titleposition
            Deprecated: Please use pie.title.position instead.
            Specifies the location of the `title`. Note that the
            title's position used to be set by the now deprecated
            `titleposition` attribute.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values of the sectors. If omitted, we count
            occurrences of each label.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Pie
        """
        new_trace = Pie(
            customdata=customdata,
            customdatasrc=customdatasrc,
            direction=direction,
            dlabel=dlabel,
            domain=domain,
            hole=hole,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            label0=label0,
            labels=labels,
            labelssrc=labelssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            pull=pull,
            pullsrc=pullsrc,
            rotation=rotation,
            scalegroup=scalegroup,
            showlegend=showlegend,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            title=title,
            titlefont=titlefont,
            titleposition=titleposition,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_pointcloud(
        self,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        indices=None,
        indicessrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbounds=None,
        xboundssrc=None,
        xsrc=None,
        xy=None,
        xysrc=None,
        y=None,
        yaxis=None,
        ybounds=None,
        yboundssrc=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Pointcloud trace
        
        The data visualized as a point cloud set in `x` and `y` using
        the WebGl plotting engine.

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.pointcloud.Hoverlabel instance or
            dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        indices
            A sequential value, 0..n, supply it to avoid creating
            this array inside plotting. If specified, it must be a
            typed `Int32Array` array. Its length must be equal to
            or greater than the number of points. For the best
            performance and memory use, create one large `indices`
            typed array that is guaranteed to be at least as long
            as the largest number of points during use, and reuse
            it on each `Plotly.restyle()` call.
        indicessrc
            Sets the source reference on plot.ly for  indices .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.pointcloud.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.pointcloud.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbounds
            Specify `xbounds` in the shape of `[xMin, xMax] to
            avoid looping through the `xy` typed array. Use it in
            conjunction with `xy` and `ybounds` for the performance
            benefits.
        xboundssrc
            Sets the source reference on plot.ly for  xbounds .
        xsrc
            Sets the source reference on plot.ly for  x .
        xy
            Faster alternative to specifying `x` and `y`
            separately. If supplied, it must be a typed
            `Float32Array` array that represents points such that
            `xy[i * 2] = x[i]` and `xy[i * 2 + 1] = y[i]`
        xysrc
            Sets the source reference on plot.ly for  xy .
        y
            Sets the y coordinates.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybounds
            Specify `ybounds` in the shape of `[yMin, yMax] to
            avoid looping through the `xy` typed array. Use it in
            conjunction with `xy` and `xbounds` for the performance
            benefits.
        yboundssrc
            Sets the source reference on plot.ly for  ybounds .
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Pointcloud
        """
        new_trace = Pointcloud(
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            indices=indices,
            indicessrc=indicessrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbounds=xbounds,
            xboundssrc=xboundssrc,
            xsrc=xsrc,
            xy=xy,
            xysrc=xysrc,
            y=y,
            yaxis=yaxis,
            ybounds=ybounds,
            yboundssrc=yboundssrc,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_sankey(
        self,
        arrangement=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        link=None,
        meta=None,
        metasrc=None,
        name=None,
        node=None,
        orientation=None,
        selectedpoints=None,
        stream=None,
        textfont=None,
        uid=None,
        uirevision=None,
        valueformat=None,
        valuesuffix=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Sankey trace
        
        Sankey plots for network flow data analysis. The nodes are
        specified in `nodes` and the links between sources and targets
        in `links`. The colors are set in `nodes[i].color` and
        `links[i].color`, otherwise defaults are used.

        Parameters
        ----------
        arrangement
            If value is `snap` (the default), the node arrangement
            is assisted by automatic snapping of elements to
            preserve space between nodes specified via `nodepad`.
            If value is `perpendicular`, the nodes can only move
            along a line perpendicular to the flow. If value is
            `freeform`, the nodes can freely move on the plane. If
            value is `fixed`, the nodes are stationary.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.sankey.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired. Note that this attribute is
            superseded by `node.hoverinfo` and `node.hoverinfo` for
            nodes and links respectively.
        hoverlabel
            plotly.graph_objs.sankey.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        link
            The links of the Sankey plot.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        node
            The nodes of the Sankey plot.
        orientation
            Sets the orientation of the Sankey diagram.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        stream
            plotly.graph_objs.sankey.Stream instance or dict with
            compatible properties
        textfont
            Sets the font for node labels
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        valuesuffix
            Adds a unit to follow the value in the hover tooltip.
            Add a space if a separation is necessary from the
            value.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Sankey
        """
        new_trace = Sankey(
            arrangement=arrangement,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            link=link,
            meta=meta,
            metasrc=metasrc,
            name=name,
            node=node,
            orientation=orientation,
            selectedpoints=selectedpoints,
            stream=stream,
            textfont=textfont,
            uid=uid,
            uirevision=uirevision,
            valueformat=valueformat,
            valuesuffix=valuesuffix,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatter(
        self,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        groupnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        orientation=None,
        r=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stackgaps=None,
        stackgroup=None,
        stream=None,
        t=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        tsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Scatter trace
        
        The scatter trace type encompasses line charts, scatter charts,
        text charts, and bubble charts. The data visualized as scatter
        point or lines is set in `x` and `y`. Text (appearing either on
        the chart or on hover only) is via `text`. Bubble charts are
        achieved by setting `marker.size` and/or `marker.color` to
        numerical arrays.

        Parameters
        ----------
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            plotly.graph_objs.scatter.ErrorX instance or dict with
            compatible properties
        error_y
            plotly.graph_objs.scatter.ErrorY instance or dict with
            compatible properties
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        groupnorm
            Only relevant when `stackgroup` is used, and only the
            first `groupnorm` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Sets the normalization for the sum of
            this `stackgroup`. With "fraction", the value of each
            trace at each location is divided by the sum of all
            trace values at that location. "percent" is the same
            but multiplied by 100 to show percentages. If there are
            multiple subplots, or multiple `stackgroup`s on one
            subplot, each will be normalized within its own set.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scatter.Hoverlabel instance or dict
            with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scatter.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.scatter.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        orientation
            Only relevant when `stackgroup` is used, and only the
            first `orientation` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Sets the stacking direction. With "v"
            ("h"), the y (x) values of subsequent traces are added.
            Also affects the default value of `fill`.
        r
            r coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the radial
            coordinatesfor legacy polar chart only.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.scatter.Selected instance or dict
            with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stackgaps
            Only relevant when `stackgroup` is used, and only the
            first `stackgaps` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Determines how we handle locations at
            which other traces in this group have data but this one
            does not. With *infer zero* we insert a zero at these
            locations. With "interpolate" we linearly interpolate
            between existing values, and extrapolate a constant
            beyond the existing values.
        stackgroup
            Set several scatter traces (on the same subplot) to the
            same stackgroup in order to add their y values (or
            their x values if `orientation` is "h"). If blank or
            omitted this trace will not be stacked. Stacking also
            turns `fill` on by default, using "tonexty" ("tonextx")
            if `orientation` is "h" ("v") and sets the default
            `mode` to "lines" irrespective of point count. You can
            only stack on a numeric (linear or log) axis. Traces in
            a `stackgroup` will only fill to (or be filled to)
            other traces in the same group. With multiple
            `stackgroup`s or some traces stacked and some not, if
            fill-linked traces are not already consecutive, the
            later ones will be pushed down in the drawing order.
        stream
            plotly.graph_objs.scatter.Stream instance or dict with
            compatible properties
        t
            t coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the
            angular coordinatesfor legacy polar chart only.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        tsrc
            Sets the source reference on plot.ly for  t .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scatter.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Scatter
        """
        new_trace = Scatter(
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            fill=fill,
            fillcolor=fillcolor,
            groupnorm=groupnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            orientation=orientation,
            r=r,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stackgaps=stackgaps,
            stackgroup=stackgroup,
            stream=stream,
            t=t,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            tsrc=tsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_scatter3d(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        error_z=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        projection=None,
        scene=None,
        showlegend=None,
        stream=None,
        surfaceaxis=None,
        surfacecolor=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatter3d trace
        
        The data visualized as scatter point or lines in 3D dimension
        is set in `x`, `y`, `z`. Text (appearing either on the chart or
        on hover only) is via `text`. Bubble charts are achieved by
        setting `marker.size` and/or `marker.color` Projections are
        achieved via `projection`. Surface fills are achieved via
        `surfaceaxis`.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        error_x
            plotly.graph_objs.scatter3d.ErrorX instance or dict
            with compatible properties
        error_y
            plotly.graph_objs.scatter3d.ErrorY instance or dict
            with compatible properties
        error_z
            plotly.graph_objs.scatter3d.ErrorZ instance or dict
            with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scatter3d.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets text elements associated with each (x,y,z)
            triplet. If a single string, the same string appears
            over all the data points. If an array of string, the
            items are mapped in order to the this trace's (x,y,z)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scatter3d.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.scatter3d.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        projection
            plotly.graph_objs.scatter3d.Projection instance or dict
            with compatible properties
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scatter3d.Stream instance or dict
            with compatible properties
        surfaceaxis
            If "-1", the scatter points are not fill with a surface
            If 0, 1, 2, the scatter points are filled with a
            Delaunay surface about the x, y, z respectively.
        surfacecolor
            Sets the surface fill color.
        text
            Sets text elements associated with each (x,y,z)
            triplet. If a single string, the same string appears
            over all the data points. If an array of string, the
            items are mapped in order to the this trace's (x,y,z)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
        textfont
            plotly.graph_objs.scatter3d.Textfont instance or dict
            with compatible properties
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the z coordinates.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Scatter3d
        """
        new_trace = Scatter3d(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            error_x=error_x,
            error_y=error_y,
            error_z=error_z,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            projection=projection,
            scene=scene,
            showlegend=showlegend,
            stream=stream,
            surfaceaxis=surfaceaxis,
            surfacecolor=surfacecolor,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattercarpet(
        self,
        a=None,
        asrc=None,
        b=None,
        bsrc=None,
        carpet=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Scattercarpet trace
        
        Plots a scatter trace on either the first carpet axis or the
        carpet axis with a matching `carpet` attribute.

        Parameters
        ----------
        a
            Sets the a-axis coordinates.
        asrc
            Sets the source reference on plot.ly for  a .
        b
            Sets the b-axis coordinates.
        bsrc
            Sets the source reference on plot.ly for  b .
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `scattercontour` traces can specify a carpet plot
            on which they lie
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterternary has a subset
            of the options available to scatter. "toself" connects
            the endpoints of the trace (or each segment of the
            trace if it has gaps) into a closed shape. "tonext"
            fills the space between two traces if one completely
            encloses the other (eg consecutive contour lines), and
            behaves like "toself" if there is no trace before it.
            "tonext" should not be used if one trace does not
            enclose the other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scattercarpet.Hoverlabel instance or
            dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (a,b)
            point. If a single string, the same string appears over
            all the data points. If an array of strings, the items
            are mapped in order to the the data points in (a,b). To
            be seen, trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scattercarpet.Line instance or dict
            with compatible properties
        marker
            plotly.graph_objs.scattercarpet.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.scattercarpet.Selected instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scattercarpet.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (a,b) point. If
            a single string, the same string appears over all the
            data points. If an array of strings, the items are
            mapped in order to the the data points in (a,b). If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scattercarpet.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Scattercarpet
        """
        new_trace = Scattercarpet(
            a=a,
            asrc=asrc,
            b=b,
            bsrc=bsrc,
            carpet=carpet,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            xaxis=xaxis,
            yaxis=yaxis,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_scattergeo(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        geo=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legendgroup=None,
        line=None,
        locationmode=None,
        locations=None,
        locationssrc=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scattergeo trace
        
        The data visualized as scatter point or lines on a geographic
        map is provided either by longitude/latitude pairs in `lon` and
        `lat` respectively or by geographic location IDs or names in
        `locations`.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        geo
            Sets a reference between this trace's geospatial
            coordinates and a geographic map. If "geo" (the default
            value), the geospatial coordinates refer to
            `layout.geo`. If "geo2", the geospatial coordinates
            refer to `layout.geo2`, and so on.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scattergeo.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (lon,lat)
            pair or item in `locations`. If a single string, the
            same string appears over all the data points. If an
            array of string, the items are mapped in order to the
            this trace's (lon,lat) or `locations` coordinates. To
            be seen, trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on plot.ly for  lat .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scattergeo.Line instance or dict with
            compatible properties
        locationmode
            Determines the set of locations used to match entries
            in `locations` to regions on the map.
        locations
            Sets the coordinates via location IDs or names.
            Coordinates correspond to the centroid of each location
            given. See `locationmode` for more info.
        locationssrc
            Sets the source reference on plot.ly for  locations .
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on plot.ly for  lon .
        marker
            plotly.graph_objs.scattergeo.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.scattergeo.Selected instance or dict
            with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scattergeo.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (lon,lat) pair
            or item in `locations`. If a single string, the same
            string appears over all the data points. If an array of
            string, the items are mapped in order to the this
            trace's (lon,lat) or `locations` coordinates. If trace
            `hoverinfo` contains a "text" flag and "hovertext" is
            not set, these elements will be seen in the hover
            labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scattergeo.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Scattergeo
        """
        new_trace = Scattergeo(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            geo=geo,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legendgroup=legendgroup,
            line=line,
            locationmode=locationmode,
            locations=locations,
            locationssrc=locationssrc,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattergl(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Scattergl trace
        
        The data visualized as scatter point or lines is set in `x` and
        `y` using the WebGL plotting engine. Bubble charts are achieved
        by setting `marker.size` and/or `marker.color` to a numerical
        arrays.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            plotly.graph_objs.scattergl.ErrorX instance or dict
            with compatible properties
        error_y
            plotly.graph_objs.scattergl.ErrorY instance or dict
            with compatible properties
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scattergl.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scattergl.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.scattergl.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.scattergl.Selected instance or dict
            with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scattergl.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scattergl.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Scattergl
        """
        new_trace = Scattergl(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_scattermapbox(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legendgroup=None,
        line=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scattermapbox trace
        
        The data visualized as scatter point, lines or marker symbols
        on a Mapbox GL geographic map is provided by longitude/latitude
        pairs in `lon` and `lat`.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scattermapbox.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (lon,lat)
            pair If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (lon,lat)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on plot.ly for  lat .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scattermapbox.Line instance or dict
            with compatible properties
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on plot.ly for  lon .
        marker
            plotly.graph_objs.scattermapbox.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.scattermapbox.Selected instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scattermapbox.Stream instance or dict
            with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a mapbox subplot. If "mapbox" (the default value),
            the data refer to `layout.mapbox`. If "mapbox2", the
            data refer to `layout.mapbox2`, and so on.
        text
            Sets text elements associated with each (lon,lat) pair
            If a single string, the same string appears over all
            the data points. If an array of string, the items are
            mapped in order to the this trace's (lon,lat)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
        textfont
            Sets the icon text font (color=mapbox.layer.paint.text-
            color, size=mapbox.layer.layout.text-size). Has an
            effect only when `type` is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scattermapbox.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Scattermapbox
        """
        new_trace = Scattermapbox(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legendgroup=legendgroup,
            line=line,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterpolar(
        self,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatterpolar trace
        
        The scatterpolar trace type encompasses line charts, scatter
        charts, text charts, and bubble charts in polar coordinates.
        The data visualized as scatter point or lines is set in `r`
        (radial) and `theta` (angular) coordinates Text (appearing
        either on the chart or on hover only) is via `text`. Bubble
        charts are achieved by setting `marker.size` and/or
        `marker.color` to numerical arrays.

        Parameters
        ----------
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterpolar has a subset of
            the options available to scatter. "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scatterpolar.Hoverlabel instance or
            dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scatterpolar.Line instance or dict
            with compatible properties
        marker
            plotly.graph_objs.scatterpolar.Marker instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.scatterpolar.Selected instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scatterpolar.Stream instance or dict
            with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on plot.ly for  theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scatterpolar.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Scatterpolar
        """
        new_trace = Scatterpolar(
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterpolargl(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatterpolargl trace
        
        The scatterpolargl trace type encompasses line charts, scatter
        charts, and bubble charts in polar coordinates using the WebGL
        plotting engine. The data visualized as scatter point or lines
        is set in `r` (radial) and `theta` (angular) coordinates Bubble
        charts are achieved by setting `marker.size` and/or
        `marker.color` to numerical arrays.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scatterpolargl.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scatterpolargl.Line instance or dict
            with compatible properties
        marker
            plotly.graph_objs.scatterpolargl.Marker instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.scatterpolargl.Selected instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scatterpolargl.Stream instance or
            dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on plot.ly for  theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scatterpolargl.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Scatterpolargl
        """
        new_trace = Scatterpolargl(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterternary(
        self,
        a=None,
        asrc=None,
        b=None,
        bsrc=None,
        c=None,
        cliponaxis=None,
        connectgaps=None,
        csrc=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        sum=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatterternary trace
        
        Provides similar functionality to the "scatter" type but on a
        ternary phase diagram. The data is provided by at least two
        arrays out of `a`, `b`, `c` triplets.

        Parameters
        ----------
        a
            Sets the quantity of component `a` in each data point.
            If `a`, `b`, and `c` are all provided, they need not be
            normalized, only the relative values matter. If only
            two arrays are provided they must be normalized to
            match `ternary<i>.sum`.
        asrc
            Sets the source reference on plot.ly for  a .
        b
            Sets the quantity of component `a` in each data point.
            If `a`, `b`, and `c` are all provided, they need not be
            normalized, only the relative values matter. If only
            two arrays are provided they must be normalized to
            match `ternary<i>.sum`.
        bsrc
            Sets the source reference on plot.ly for  b .
        c
            Sets the quantity of component `a` in each data point.
            If `a`, `b`, and `c` are all provided, they need not be
            normalized, only the relative values matter. If only
            two arrays are provided they must be normalized to
            match `ternary<i>.sum`.
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        csrc
            Sets the source reference on plot.ly for  c .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterternary has a subset
            of the options available to scatter. "toself" connects
            the endpoints of the trace (or each segment of the
            trace if it has gaps) into a closed shape. "tonext"
            fills the space between two traces if one completely
            encloses the other (eg consecutive contour lines), and
            behaves like "toself" if there is no trace before it.
            "tonext" should not be used if one trace does not
            enclose the other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.scatterternary.Hoverlabel instance or
            dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (a,b,c)
            point. If a single string, the same string appears over
            all the data points. If an array of strings, the items
            are mapped in order to the the data points in (a,b,c).
            To be seen, trace `hoverinfo` must contain a "text"
            flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.scatterternary.Line instance or dict
            with compatible properties
        marker
            plotly.graph_objs.scatterternary.Marker instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.scatterternary.Selected instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.scatterternary.Stream instance or
            dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a ternary subplot. If "ternary" (the default
            value), the data refer to `layout.ternary`. If
            "ternary2", the data refer to `layout.ternary2`, and so
            on.
        sum
            The number each triplet should sum to, if only two of
            `a`, `b`, and `c` are provided. This overrides
            `ternary<i>.sum` to normalize this specific trace, but
            does not affect the values displayed on the axes. 0 (or
            missing) means to use ternary<i>.sum
        text
            Sets text elements associated with each (a,b,c) point.
            If a single string, the same string appears over all
            the data points. If an array of strings, the items are
            mapped in order to the the data points in (a,b,c). If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.scatterternary.Unselected instance or
            dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Scatterternary
        """
        new_trace = Scatterternary(
            a=a,
            asrc=asrc,
            b=b,
            bsrc=bsrc,
            c=c,
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            csrc=csrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            sum=sum,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_splom(
        self,
        customdata=None,
        customdatasrc=None,
        diagonal=None,
        dimensions=None,
        dimensiondefaults=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showlowerhalf=None,
        showupperhalf=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        xaxes=None,
        yaxes=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Splom trace
        
        Splom traces generate scatter plot matrix visualizations. Each
        splom `dimensions` items correspond to a generated axis. Values
        for each of those dimensions are set in `dimensions[i].values`.
        Splom traces support all `scattergl` marker style attributes.
        Specify `layout.grid` attributes and/or layout x-axis and
        y-axis attributes for more control over the axis positioning
        and style.

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        diagonal
            plotly.graph_objs.splom.Diagonal instance or dict with
            compatible properties
        dimensions
            plotly.graph_objs.splom.Dimension instance or dict with
            compatible properties
        dimensiondefaults
            When used in a template (as
            layout.template.data.splom.dimensiondefaults), sets the
            default property values to use for elements of
            splom.dimensions
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.splom.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.splom.Marker instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.splom.Selected instance or dict with
            compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showlowerhalf
            Determines whether or not subplots on the lower half
            from the diagonal are displayed.
        showupperhalf
            Determines whether or not subplots on the upper half
            from the diagonal are displayed.
        stream
            plotly.graph_objs.splom.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each (x,y) pair to
            appear on hover. If a single string, the same string
            appears over all the data points. If an array of
            string, the items are mapped in order to the this
            trace's (x,y) coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.splom.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxes
            Sets the list of x axes corresponding to dimensions of
            this splom trace. By default, a splom will match the
            first N xaxes where N is the number of input
            dimensions. Note that, in case where `diagonal.visible`
            is false and `showupperhalf` or `showlowerhalf` is
            false, this splom trace will generate one less x-axis
            and one less y-axis.
        yaxes
            Sets the list of y axes corresponding to dimensions of
            this splom trace. By default, a splom will match the
            first N yaxes where N is the number of input
            dimensions. Note that, in case where `diagonal.visible`
            is false and `showupperhalf` or `showlowerhalf` is
            false, this splom trace will generate one less x-axis
            and one less y-axis.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Splom
        """
        new_trace = Splom(
            customdata=customdata,
            customdatasrc=customdatasrc,
            diagonal=diagonal,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showlowerhalf=showlowerhalf,
            showupperhalf=showupperhalf,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            xaxes=xaxes,
            yaxes=yaxes,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_streamtube(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        ids=None,
        idssrc=None,
        lighting=None,
        lightposition=None,
        maxdisplayed=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showscale=None,
        sizeref=None,
        starts=None,
        stream=None,
        text=None,
        u=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        visible=None,
        vsrc=None,
        w=None,
        wsrc=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Streamtube trace
        
        Use a streamtube trace to visualize flow in a vector field.
        Specify a vector field using 6 1D arrays of equal length, 3
        position arrays `x`, `y` and `z` and 3 vector component arrays
        `u`, `v`, and `w`.  By default, the tubes' starting positions
        will be cut from the vector field's x-z plane at its minimum y
        value. To specify your own starting position, use attributes
        `starts.x`, `starts.y` and `starts.z`.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here u/v/w norm) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as u/v/w norm. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.streamtube.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.streamtube.Hoverlabel instance or
            dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available. variables `tubex`, `tubey`, `tubez`,
            `tubeu`, `tubev`, `tubew`, `norm` and `divergence`.
            Anything contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        lighting
            plotly.graph_objs.streamtube.Lighting instance or dict
            with compatible properties
        lightposition
            plotly.graph_objs.streamtube.Lightposition instance or
            dict with compatible properties
        maxdisplayed
            The maximum number of displayed segments in a
            streamtube.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        sizeref
            The scaling factor for the streamtubes. The default is
            1, which avoids two max divergence tubes from touching
            at adjacent starting positions.
        starts
            plotly.graph_objs.streamtube.Starts instance or dict
            with compatible properties
        stream
            plotly.graph_objs.streamtube.Stream instance or dict
            with compatible properties
        text
            Sets a text element associated with this trace. If
            trace `hoverinfo` contains a "text" flag, this text
            element will be seen in all hover labels. Note that
            streamtube traces do not support array `text` values.
        u
            Sets the x components of the vector field.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        usrc
            Sets the source reference on plot.ly for  u .
        v
            Sets the y components of the vector field.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        vsrc
            Sets the source reference on plot.ly for  v .
        w
            Sets the z components of the vector field.
        wsrc
            Sets the source reference on plot.ly for  w .
        x
            Sets the x coordinates of the vector field.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates of the vector field.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the z coordinates of the vector field.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Streamtube
        """
        new_trace = Streamtube(
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            ids=ids,
            idssrc=idssrc,
            lighting=lighting,
            lightposition=lightposition,
            maxdisplayed=maxdisplayed,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showscale=showscale,
            sizeref=sizeref,
            starts=starts,
            stream=stream,
            text=text,
            u=u,
            uid=uid,
            uirevision=uirevision,
            usrc=usrc,
            v=v,
            visible=visible,
            vsrc=vsrc,
            w=w,
            wsrc=wsrc,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_sunburst(
        self,
        branchvalues=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        labels=None,
        labelssrc=None,
        leaf=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Sunburst trace
        
        Visualize hierarchal data spanning outward radially from root
        to leaves. The sunburst sectors are determined by the entries
        in "labels" or "ids" and in "parents".

        Parameters
        ----------
        branchvalues
            Determines how the items in `values` are summed. When
            set to "total", items in `values` are taken to be value
            of all its descendants. When set to "remainder", items
            in `values` corresponding to the root and the branches
            sectors are taken to be the extra part not part of the
            sum of the values at their leaves.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.sunburst.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.sunburst.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        labels
            Sets the labels of each of the sunburst sectors.
        labelssrc
            Sets the source reference on plot.ly for  labels .
        leaf
            plotly.graph_objs.sunburst.Leaf instance or dict with
            compatible properties
        level
            Sets the level from which this sunburst trace hierarchy
            is rendered. Set `level` to `''` to start the sunburst
            from the root node in the hierarchy. Must be an "id" if
            `ids` is filled in, otherwise plotly attempts to find a
            matching item in `labels`.
        marker
            plotly.graph_objs.sunburst.Marker instance or dict with
            compatible properties
        maxdepth
            Sets the number of rendered sunburst rings from any
            given `level`. Set `maxdepth` to "-1" to render all the
            levels in the hierarchy.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector.
        parents
            Sets the parent sectors for each of the sunburst
            sectors. Empty string items '' are understood to
            reference the root node in the hierarchy. If `ids` is
            filled, `parents` items are understood to be "ids"
            themselves. When `ids` is not set, plotly attempts to
            find matching items in `labels`, but beware they must
            be unique.
        parentssrc
            Sets the source reference on plot.ly for  parents .
        stream
            plotly.graph_objs.sunburst.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values associated with each of the sunburst
            sectors. Use with `branchvalues` to determine how the
            values are summed.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Sunburst
        """
        new_trace = Sunburst(
            branchvalues=branchvalues,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            labels=labels,
            labelssrc=labelssrc,
            leaf=leaf,
            level=level,
            marker=marker,
            maxdepth=maxdepth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            parents=parents,
            parentssrc=parentssrc,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_surface(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        hidesurface=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showscale=None,
        stream=None,
        surfacecolor=None,
        surfacecolorsrc=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Surface trace
        
        The data the describes the coordinates of the surface is set in
        `z`. Data in `z` should be a 2D list. Coordinates in `x` and
        `y` can either be 1D lists or 2D lists (e.g. to graph
        parametric surfaces). If not provided in `x` and `y`, the x and
        y coordinates are assumed to be linear starting at 0 with a
        unit step. The color scale corresponds to the `z` values by
        default. For custom color scales, use `surfacecolor` which
        should be a 2D list, where its bounds can be controlled using
        `cmin` and `cmax`.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here z or surfacecolor)
            or the bounds set in `cmin` and `cmax`  Defaults to
            `false` when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as z or surfacecolor and if set,
            `cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as z or surfacecolor.
            Has no effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as z or surfacecolor and if set,
            `cmax` must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.surface.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in.
        contours
            plotly.graph_objs.surface.Contours instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        hidesurface
            Determines whether or not a surface is drawn. For
            example, set `hidesurface` to False `contours.x.show`
            to True and `contours.y.show` to True to draw a wire
            frame plot.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.surface.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        lighting
            plotly.graph_objs.surface.Lighting instance or dict
            with compatible properties
        lightposition
            plotly.graph_objs.surface.Lightposition instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.surface.Stream instance or dict with
            compatible properties
        surfacecolor
            Sets the surface color values, used for setting a color
            scale independent of `z`.
        surfacecolorsrc
            Sets the source reference on plot.ly for  surfacecolor
            .
        text
            Sets the text elements associated with each z value. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the z coordinates.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Surface
        """
        new_trace = Surface(
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hidesurface=hidesurface,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showscale=showscale,
            stream=stream,
            surfacecolor=surfacecolor,
            surfacecolorsrc=surfacecolorsrc,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_table(
        self,
        cells=None,
        columnorder=None,
        columnordersrc=None,
        columnwidth=None,
        columnwidthsrc=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        header=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Table trace
        
        Table view for detailed data viewing. The data are arranged in
        a grid of rows and columns. Most styling can be specified for
        columns, rows or individual cells. Table is using a column-
        major order, ie. the grid is represented as a vector of column
        vectors.

        Parameters
        ----------
        cells
            plotly.graph_objs.table.Cells instance or dict with
            compatible properties
        columnorder
            Specifies the rendered order of the data columns; for
            example, a value `2` at position `0` means that column
            index `0` in the data will be rendered as the third
            column, as columns have an index base of zero.
        columnordersrc
            Sets the source reference on plot.ly for  columnorder .
        columnwidth
            The width of columns expressed as a ratio. Columns fill
            the available width in proportion of their specified
            column widths.
        columnwidthsrc
            Sets the source reference on plot.ly for  columnwidth .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.table.Domain instance or dict with
            compatible properties
        header
            plotly.graph_objs.table.Header instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.table.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        stream
            plotly.graph_objs.table.Stream instance or dict with
            compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Table
        """
        new_trace = Table(
            cells=cells,
            columnorder=columnorder,
            columnordersrc=columnordersrc,
            columnwidth=columnwidth,
            columnwidthsrc=columnwidthsrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            header=header,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_violin(
        self,
        alignmentgroup=None,
        bandwidth=None,
        box=None,
        customdata=None,
        customdatasrc=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legendgroup=None,
        line=None,
        marker=None,
        meanline=None,
        meta=None,
        metasrc=None,
        name=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        points=None,
        scalegroup=None,
        scalemode=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        side=None,
        span=None,
        spanmode=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Violin trace
        
        In vertical (horizontal) violin plots, statistics are computed
        using `y` (`x`) values. By supplying an `x` (`y`) array, one
        violin per distinct x (y) value is drawn If no `x` (`y`) list
        is provided, a single violin is drawn. That violin position is
        then positioned with with `name` or with `x0` (`y0`) if
        provided.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        bandwidth
            Sets the bandwidth used to compute the kernel density
            estimate. By default, the bandwidth is determined by
            Silverman's rule of thumb.
        box
            plotly.graph_objs.violin.Box instance or dict with
            compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.violin.Hoverlabel instance or dict
            with compatible properties
        hoveron
            Do the hover effects highlight individual violins or
            sample points or the kernel density estimate or any
            combination of them?
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the violins.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.violin.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.violin.Marker instance or dict with
            compatible properties
        meanline
            plotly.graph_objs.violin.Meanline instance or dict with
            compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For violin traces, the name
            will also be used for the position coordinate, if `x`
            and `x0` (`y` and `y0` if horizontal) are missing and
            the position axis is categorical. Note that the trace
            name is also used as a default value for attribute
            `scalegroup` (please see its description for details).
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the violin(s). If "v" ("h"),
            the distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the violins. If 0, the sample points are places over
            the center of the violins. Positive (negative) values
            correspond to positions to the right (left) for
            vertical violins and above (below) for horizontal
            violins.
        points
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the violins are shown with no sample
            points
        scalegroup
            If there are multiple violins that should be sized
            according to to some metric (see `scalemode`), link
            them by providing a non-empty group id here shared by
            every trace in the same group. If a violin's `width` is
            undefined, `scalegroup` will default to the trace's
            name. In this case, violins with the same names will be
            linked together
        scalemode
            Sets the metric by which the width of each violin is
            determined."width" means each violin has the same (max)
            width*count* means the violins are scaled by the number
            of sample points makingup each violin.
        selected
            plotly.graph_objs.violin.Selected instance or dict with
            compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        side
            Determines on which side of the position value the
            density function making up one half of a violin is
            plotted. Useful when comparing two violin traces under
            "overlay" mode, where one trace has `side` set to
            "positive" and the other to "negative".
        span
            Sets the span in data space for which the density
            function will be computed. Has an effect only when
            `spanmode` is set to "manual".
        spanmode
            Sets the method by which the span in data space where
            the density function will be computed. "soft" means the
            span goes from the sample's minimum value minus two
            bandwidths to the sample's maximum value plus two
            bandwidths. "hard" means the span goes from the
            sample's minimum to its maximum value. For custom span
            settings, use mode "manual" and fill in the `span`
            attribute.
        stream
            plotly.graph_objs.violin.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            plotly.graph_objs.violin.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the width of the violin in data coordinates. If 0
            (default value) the width is automatically selected
            based on the positions of other violin traces in the
            same subplot.
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate of the box. See overview for more
            info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate of the box. See overview for more
            info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Violin
        """
        new_trace = Violin(
            alignmentgroup=alignmentgroup,
            bandwidth=bandwidth,
            box=box,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            jitter=jitter,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meanline=meanline,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            pointpos=pointpos,
            points=points,
            scalegroup=scalegroup,
            scalemode=scalemode,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            side=side,
            span=span,
            spanmode=spanmode,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def add_volume(
        self,
        autocolorscale=None,
        caps=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        isomax=None,
        isomin=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        opacityscale=None,
        reversescale=None,
        scene=None,
        showscale=None,
        slices=None,
        spaceframe=None,
        stream=None,
        surface=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        value=None,
        valuesrc=None,
        visible=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Volume trace
        
        Draws volume trace between iso-min and iso-max values with
        coordinates given by four 1-dimensional arrays containing the
        `value`, `x`, `y` and `z` of every vertex of a uniform or non-
        uniform 3-D grid. Horizontal or vertical slices, caps as well
        as spaceframe between iso-min and iso-max values could also be
        drawn using this trace.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        caps
            plotly.graph_objs.volume.Caps instance or dict with
            compatible properties
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `value`) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `value` and if set, `cmin` must
            be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `value`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `value` and if set, `cmax` must
            be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objs.volume.ColorBar instance or dict with
            compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contour
            plotly.graph_objs.volume.Contour instance or dict with
            compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.volume.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        isomax
            Sets the maximum boundary for iso-surface plot.
        isomin
            Sets the minimum boundary for iso-surface plot.
        lighting
            plotly.graph_objs.volume.Lighting instance or dict with
            compatible properties
        lightposition
            plotly.graph_objs.volume.Lightposition instance or dict
            with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        opacityscale
            Sets the opacityscale. The opacityscale must be an
            array containing arrays mapping a normalized value to
            an opacity value. At minimum, a mapping for the lowest
            (0) and highest (1) values are required. For example,
            `[[0, 1], [0.5, 0.2], [1, 1]]` means that higher/lower
            values would have higher opacity values and those in
            the middle would be more transparent Alternatively,
            `opacityscale` may be a palette name string of the
            following list: 'min', 'max', 'extremes' and 'uniform'.
            The default is 'uniform'.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        slices
            plotly.graph_objs.volume.Slices instance or dict with
            compatible properties
        spaceframe
            plotly.graph_objs.volume.Spaceframe instance or dict
            with compatible properties
        stream
            plotly.graph_objs.volume.Stream instance or dict with
            compatible properties
        surface
            plotly.graph_objs.volume.Surface instance or dict with
            compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the 4th dimension (value) of the vertices.
        valuesrc
            Sets the source reference on plot.ly for  value .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices on X axis.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the Y coordinates of the vertices on Y axis.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the Z coordinates of the vertices on Z axis.
        zsrc
            Sets the source reference on plot.ly for  z .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Volume
        """
        new_trace = Volume(
            autocolorscale=autocolorscale,
            caps=caps,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            isomax=isomax,
            isomin=isomin,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            opacityscale=opacityscale,
            reversescale=reversescale,
            scene=scene,
            showscale=showscale,
            slices=slices,
            spaceframe=spaceframe,
            stream=stream,
            surface=surface,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            value=value,
            valuesrc=valuesrc,
            visible=visible,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_waterfall(
        self,
        alignmentgroup=None,
        base=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        insidetextanchor=None,
        insidetextfont=None,
        legendgroup=None,
        measure=None,
        measuresrc=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        totals=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Waterfall trace
        
        Draws waterfall trace which is useful graph to displays the
        contribution of various elements (either positive or negative)
        in a bar chart. The data visualized by the span of the bars is
        set in `y` if `orientation` is set th "v" (the default) and the
        labels are set in `x`. By setting `orientation` to "h", the
        roles are interchanged.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        base
            Sets where the bar base is drawn (in position axis
            units).
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        connector
            plotly.graph_objs.waterfall.Connector instance or dict
            with compatible properties
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        decreasing
            plotly.graph_objs.waterfall.Decreasing instance or dict
            with compatible properties
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.waterfall.Hoverlabel instance or dict
            with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". See https://github.com/d3/d3-format
            /blob/master/README.md#locale_format for details on the
            formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plot.ly/javascript/plotlyjs-events/#event-data.
            Additionally, every attributes that can be specified
            per-point (the ones that are `arrayOk: true`) are
            available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on plot.ly for  hovertemplate
            .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        increasing
            plotly.graph_objs.waterfall.Increasing instance or dict
            with compatible properties
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        measure
            An array containing types of values. By default the
            values are considered as 'relative'. However; it is
            possible to use 'total' to compute the sums. Also
            'absolute' could be applied to reset the computed total
            or to declare an initial value where needed.
        measuresrc
            Sets the source reference on plot.ly for  measure .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on plot.ly for  meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.waterfall.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textinfo
            Determines which trace information appear on the graph.
            In the case of having multiple waterfalls, totals are
            computed separately (per trace).
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        totals
            plotly.graph_objs.waterfall.Totals instance or dict
            with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        widthsrc
            Sets the source reference on plot.ly for  width .
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Waterfall
        """
        new_trace = Waterfall(
            alignmentgroup=alignmentgroup,
            base=base,
            cliponaxis=cliponaxis,
            connector=connector,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legendgroup=legendgroup,
            measure=measure,
            measuresrc=measuresrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            offsetsrc=offsetsrc,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            totals=totals,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(
            new_trace, row=row, col=col, secondary_y=secondary_y
        )

    def select_coloraxes(self, selector=None, row=None, col=None):
        """
        Select coloraxis subplot objects from a particular subplot cell
        and/or coloraxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the coloraxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'coloraxis', selector, row, col
        )

    def for_each_coloraxis(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all coloraxis objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single coloraxis object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_coloraxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_coloraxes(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all coloraxis objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            coloraxis objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            coloraxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_coloraxes(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_geos(self, selector=None, row=None, col=None):
        """
        Select geo subplot objects from a particular subplot cell
        and/or geo subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the geo
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'geo', selector, row, col
        )

    def for_each_geo(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all geo objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single geo object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_geos(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_geos(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all geo objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            geo objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            geo object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_geos(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_mapboxes(self, selector=None, row=None, col=None):
        """
        Select mapbox subplot objects from a particular subplot cell
        and/or mapbox subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the mapbox
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'mapbox', selector, row, col
        )

    def for_each_mapbox(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all mapbox objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single mapbox object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_mapboxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_mapboxes(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all mapbox objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            mapbox objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            mapbox object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_mapboxes(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_polars(self, selector=None, row=None, col=None):
        """
        Select polar subplot objects from a particular subplot cell
        and/or polar subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the polar
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'polar', selector, row, col
        )

    def for_each_polar(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all polar objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single polar object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_polars(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_polars(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all polar objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            polar objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            polar object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_polars(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_scenes(self, selector=None, row=None, col=None):
        """
        Select scene subplot objects from a particular subplot cell
        and/or scene subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the scene
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'scene', selector, row, col
        )

    def for_each_scene(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all scene objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single scene object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_scenes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_scenes(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all scene objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            scene objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            scene object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_scenes(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_ternaries(self, selector=None, row=None, col=None):
        """
        Select ternary subplot objects from a particular subplot cell
        and/or ternary subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the ternary
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'ternary', selector, row, col
        )

    def for_each_ternary(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all ternary objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single ternary object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_ternaries(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_ternaries(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all ternary objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            ternary objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            ternary object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_ternaries(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_xaxes(self, selector=None, row=None, col=None):
        """
        Select xaxis subplot objects from a particular subplot cell
        and/or xaxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the xaxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'xaxis', selector, row, col
        )

    def for_each_xaxis(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all xaxis objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single xaxis object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_xaxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_xaxes(
        self, patch=None, selector=None, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all xaxis objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            xaxis objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            xaxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_xaxes(selector=selector, row=row, col=col):
            obj.update(patch, **kwargs)

        return self

    def select_yaxes(
        self, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Select yaxis subplot objects from a particular subplot cell
        and/or yaxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition. 
            
            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the yaxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            'yaxis', selector, row, col, secondary_y=secondary_y
        )

    def for_each_yaxis(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Apply a function to all yaxis objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single yaxis object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition. 
            
            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_yaxes(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            fn(obj)

        return self

    def update_yaxes(
        self,
        patch=None,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Perform a property update operation on all yaxis objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            yaxis objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition. 
            
            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected
            yaxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_yaxes(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            obj.update(patch, **kwargs)

        return self
