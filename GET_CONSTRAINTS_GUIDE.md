# Get Constraints Tool - User Guide

## Overview

The `get_constraints` tool retrieves all available constraint values for each dimension of a dataflow, complete with Italian and English descriptions. This tool combines data from multiple sources (constraints, structure, and codelists) into a single, comprehensive response.

## How It Works

### Internal Workflow

The `get_constraints` tool internally combines three separate operations:

1. **Fetch Constraints** (availableconstraint endpoint)
   - Gets the list of valid values for each dimension
   - Only includes values that are actually available for this specific dataflow

2. **Call get_structure internally**
   - Fetches the datastructure definition
   - Builds a mapping: dimension → codelist ID
   - Example: `TYPE_OF_CROP` → `CL_AGRI_MADRE`

3. **Call get_codelist_description internally**
   - For each dimension, fetches the associated codelist
   - Retrieves Italian and English descriptions for all codes
   - Example: `APPLE` → "Apples" / "Mele"

4. **Combine and Cache**
  - Merges all data into a single response
  - Caches constraints, datastructures, and codelists with the shared metadata TTL (default: 1 month)
  - **Subsequent calls use cached data** - no API calls needed!

### Caching Strategy

Constraints, datastructures, and codelists are cached independently with the shared metadata TTL (default: 1 month):

```
First call to get_constraints:
├─ Constraint values (cached, 1 month)
├─ Datastructure (cached, 1 month) 
└─ Each codelist (cached, 1 month)

Second call to get_constraints (same dataflow):
└─ Everything from cache → instant response!
```

This means:
- First call: 2-5 seconds (fetches all data)
- Subsequent calls: < 50ms (fully cached)
- Cache shared across all tools (get_structure, get_codelist_description use same cache)

## Purpose

When working with ISTAT dataflows, you need to know:
1. What dimensions are available
2. What values each dimension can accept
3. What those values mean (descriptions in Italian and English)

The `get_constraints` tool provides all this information in one call, making it much faster and easier than calling `get_structure` and `get_codelist_description` separately for each dimension.

## Input

```json
{
  "dataflow_id": "101_1015_DF_DCSP_COLTIVAZIONI_1"
}
```

**Parameters**:
- `dataflow_id` (required): The ID of the dataflow to analyze

## Output

The tool returns a JSON structure with:
- `id_dataflow`: The dataflow ID
- `constraints`: Array of dimension constraints

Each dimension constraint contains:
- `dimension`: Dimension name (e.g., "TYPE_OF_CROP")
- `codelist`: Associated codelist ID (e.g., "CL_AGRI_MADRE")
- `values`: Array of valid codes with descriptions

Each value contains:
- `code`: The code value (e.g., "APPLE")
- `description_en`: English description (e.g., "Apples")
- `description_it`: Italian description (e.g., "Mele")

### Example Output

```json
{
  "id_dataflow": "101_1015_DF_DCSP_COLTIVAZIONI_1",
  "constraints": [
    {
      "dimension": "FREQ",
      "codelist": "CL_FREQ",
      "values": [
        {
          "code": "A",
          "description_en": "Annual",
          "description_it": "Annuale"
        }
      ]
    },
    {
      "dimension": "REF_AREA",
      "codelist": "CL_ITTER107",
      "values": [
        {
          "code": "IT",
          "description_en": "Italy",
          "description_it": "Italia"
        },
        {
          "code": "ITC1",
          "description_en": "Piedmont",
          "description_it": "Piemonte"
        }
        // ... more regions
      ]
    },
    {
      "dimension": "TYPE_OF_CROP",
      "codelist": "CL_AGRI_MADRE",
      "values": [
        {
          "code": "APPLE",
          "description_en": "Apples",
          "description_it": "Mele"
        },
        {
          "code": "WHEAT",
          "description_en": "Wheat",
          "description_it": "Grano"
        }
        // ... more crops
      ]
    },
    {
      "dimension": "TIME_PERIOD",
      "StartPeriod": "2006-01-01T00:00:00",
      "EndPeriod": "2026-12-31T23:59:59"
    }
  ]
}
```

## Usage Examples

### Example 1: Find Valid Values for Agricultural Data

**User**: "Get constraints for dataflow 101_1015_DF_DCSP_COLTIVAZIONI_1"

**Claude**: 
1. Calls `get_constraints` with the dataflow ID
2. Displays dimensions with all valid values and descriptions
3. User can see that TYPE_OF_CROP accepts values like APPLE, WHEAT, RICE, etc.

### Example 2: Discover Regional Codes

**User**: "What regions are available in the population dataflow?"

**Claude**:
1. First uses `discover_dataflows` to find population dataflows
2. Uses `get_constraints` on the selected dataflow
3. Looks at the REF_AREA dimension to show all available regions with Italian and English names

### Example 3: Build Query Filters

**User**: "I want to get apple production data for Piedmont region from 2020 to 2023"

**Claude**:
1. Uses `get_constraints` to verify valid values:
   - TYPE_OF_CROP: Finds "APPLE" code
   - REF_AREA: Finds "ITC1" (Piedmont) code
   - TIME_PERIOD: Confirms 2020-2023 is within valid range
2. Calls `get_data` with correct filters:
   ```json
   {
     "id_dataflow": "101_1015_DF_DCSP_COLTIVAZIONI_1",
     "dimension_filters": {
       "TYPE_OF_CROP": ["APPLE"],
       "REF_AREA": ["ITC1"]
     },
     "start_period": "2020",
     "end_period": "2023"
   }
   ```

## Key Features

### Complete Information in One Call

**Without get_constraints** (manual approach):
```
1. Call get_structure to find dimensions and codelists
   → 1 API call, get list of dimensions and codelist IDs
   
2. For each dimension's codelist:
   - Call get_codelist_description for CL_FREQ
   - Call get_codelist_description for CL_ITTER107
   - Call get_codelist_description for CL_AGRI_MADRE
   - ... (one call per codelist)
   → N API calls (one per dimension)
   
3. Call availableconstraint to filter valid values
   → 1 more API call
   
4. Manually match codes with descriptions
   
Total: 2 + N API calls, manual data merging required
```

**With get_constraints** (automated):
```
1. Call get_constraints once
   → Internally performs all above steps
   → Returns merged result with all descriptions
   → Everything cached for future use
   
Total: 1 tool call, 0 manual work
After first call: Everything cached, instant response!
```

### 2. Dimension Ordering

The tool preserves the correct dimension order from the datastructure definition. This is important for building queries.

### 3. Time Period Handling

The TIME_PERIOD dimension is handled specially:
- Shows StartPeriod and EndPeriod instead of individual values
- Indicates the valid time range for the dataflow

### 4. Bilingual Descriptions

All code descriptions are provided in both Italian and English, making it easier to:
- Understand what each code means
- Find the right codes for your query
- Work with international users

## Caching

Constraint-related metadata is cached with the shared metadata TTL, which defaults to **1 month** (2,592,000 seconds), because:
- Constraints rarely change
- Fetching constraints + structure + all codelists is expensive (multiple API calls)
- Faster response times for repeated queries

Related runtime settings:
- `DATAFLOWS_CACHE_TTL_SECONDS=604800`
- `METADATA_CACHE_TTL_SECONDS=2592000`
- `AVAILABLECONSTRAINT_TIMEOUT_SECONDS=180`

## Error Handling

The tool handles various error conditions:

### Invalid Dataflow ID
```
Input: { "dataflow_id": "invalid-id-with-special@chars" }
Output: "Invalid dataflow ID: invalid-id-with-special@chars"
```

### Dataflow Not Found
```
Input: { "dataflow_id": "NON_EXISTENT_DF" }
Output: "Dataflow not found: NON_EXISTENT_DF"
```

### Missing Codelist
If a codelist cannot be fetched, the tool returns codes without descriptions:
```json
{
  "dimension": "SOME_DIM",
  "codelist": "CL_MISSING",
  "values": [
    {
      "code": "VAL1",
      "description_en": "",
      "description_it": ""
    }
  ]
}
```

## Comparison with Other Tools

### get_constraints vs get_structure

| Feature | get_structure | get_constraints |
|---------|---------------|-----------------|
| Dimensions | ✅ Yes | ✅ Yes |
| Codelists | ✅ Yes | ✅ Yes |
| Valid values | ❌ No | ✅ Yes |
| Descriptions | ❌ No | ✅ Yes |
| API Calls | 1 | 1 (cached) + N codelists first time |
| Use Case | See structure | Build queries |

### get_constraints vs get_codelist_description

| Feature | get_codelist_description | get_constraints |
|---------|-------------------------|-----------------|
| Single codelist | ✅ Yes | ❌ No (all at once) |
| All codelists | ❌ No (one at a time) | ✅ Yes |
| Only valid values | ❌ No (all codes) | ✅ Yes (filtered) |
| Time range | ❌ No | ✅ Yes |
| Use Case | Explore one codelist | Complete query building |

## Best Practices

### 1. Use get_constraints as Starting Point

When exploring a new dataflow:
```
1. discover_dataflows (find dataflows)
2. get_constraints (see what's possible)  ← START HERE
3. get_data (fetch actual data)
```

### 2. Cache-Friendly Workflow

Get constraints once, reuse information:
```python
# First time - fetches from API
constraints = get_constraints("101_1015_DF_DCSP_COLTIVAZIONI_1")

# Build multiple queries using same constraints
query1 = build_query(constraints, crop="APPLE", region="IT")
query2 = build_query(constraints, crop="WHEAT", region="ITC1")
```

### 3. Filter by Descriptions

When searching for codes:
```python
# Look through constraints to find codes
constraints = get_constraints("...")
for dim in constraints:
    if dim["dimension"] == "TYPE_OF_CROP":
        # Find codes with "wheat" in description
        wheat_codes = [
            v["code"] for v in dim["values"]
            if "wheat" in v["description_en"].lower()
        ]
```

## Technical Details

### Data Flow

```
get_constraints(dataflow_id)
    ↓
1. Fetch dataflows list (cached, default 7 days)
    ↓
2. Find datastructure ID for dataflow
    ↓
3. Fetch constraints from availableconstraint endpoint (cached with shared metadata TTL, default 1 month)
    ↓
4. Fetch datastructure definition (cached with shared metadata TTL, default 1 month)
    ↓
5. For each dimension with values:
    ↓
    a. Get codelist ID from datastructure
    ↓
    b. Fetch codelist descriptions (cached with shared metadata TTL, default 1 month)
    ↓
    c. Match constraint values with descriptions
    ↓
6. Build final JSON response
    ↓
7. Return constraints with complete information
```

### Performance

- **First call**: 2-5 seconds (multiple API calls for codelists)
- **Subsequent calls**: < 50ms (fully cached)
- **Cache duration**: metadata defaults to 1 month, dataflows default to 7 days
- **Memory usage**: Minimal (codelists shared across dimensions)

## Troubleshooting

### Empty Values Array

If a dimension shows no values:
- The dimension may accept any value (no constraints)
- Check the datastructure definition with `get_structure`

### Missing Descriptions

If some codes have empty descriptions:
- The codelist may not exist in ISTAT API
- Use `get_codelist_description` to verify codelist availability

### Slow First Call

First call must fetch all codelists:
- Normal behavior for large dataflows with many dimensions
- Subsequent calls are instant (cached)
- Consider calling during setup/initialization

## Examples in Different Languages

### Python
```python
import requests

response = requests.post(
    "http://localhost:3000/call_tool",
    json={
        "name": "get_constraints",
        "arguments": {
            "dataflow_id": "101_1015_DF_DCSP_COLTIVAZIONI_1"
        }
    }
)
constraints = response.json()
```

### JavaScript
```javascript
const response = await fetch('http://localhost:3000/call_tool', {
  method: 'POST',
  body: JSON.stringify({
    name: 'get_constraints',
    arguments: {
      dataflow_id: '101_1015_DF_DCSP_COLTIVAZIONI_1'
    }
  })
});
const constraints = await response.json();
```

## See Also

- [README.md](README.md) - General usage and workflow
- [SKILLS.md](SKILLS.md) - Complete workflow examples
- API Documentation: https://esploradati.istat.it/SDMXWS/rest/availableconstraint
