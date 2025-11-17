
import React, { useEffect, useState } from 'react'
import useDebounce from '../hooks/useDebounce.js'

export default function SearchBar({ onChange }) {
  const [value, setValue] = useState('')

  return (
    <input
      aria-label="search"
      placeholder="Buscar..."
      value={value}
      onChange={e => {
        const val = e.target.value
        setValue(val)
        onChange?.(val)
      }}
      style={{width:'100%', padding:'12px', border:'1px solid #ccc', borderRadius:8}}
    />
  )
}
